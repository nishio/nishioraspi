import pykintone
from pykintone import model
import warnings

class Value(model.kintoneModel):
    def __init__(self):
        super(Value, self).__init__()
        self.value = ""

TOKEN = 'mzJ3ef3m1ijBGDVsWwpje8KtBeWYyqsjAzARCKA5'
app = pykintone.app('bozuman', 15786, TOKEN, {'timeout': 10})


import serial
port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=0.1)
while True:
    v = port.read(1024)  # throw old data away
    if not v: break
		
port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3.0)
while True:
    try:
        s = port.readline()
	i = int(s.strip())
	v = Value()
	v.value = i
	app.create(v)
	print i
    except Exception, e:
        print e
	import subprocess
	subprocess.call('service networking restart', shell=True)
	import time
	time.sleep(60)
