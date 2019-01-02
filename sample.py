import serial
import time


from Adafruit_IO import Client,Feed,RequestError

ser = serial.Serial("/dev/ttyACM0")


ADAFRUIT_IO_KEY = 'API_KEY'
ADAFRUIT_IO_USERNAME = 'Username'

aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
digital = aio.feeds("Feed NAME")

data = aio.receive(digital.key)
while True:
 data = aio.receive(digital.key)
 print(data.value)
 if(data.value=="on"):
 	ser.write(b'1')
 elif(data.value=="off"):
 	ser.write(b'0')
 time.sleep(1)
