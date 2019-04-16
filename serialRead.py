import serial
from gpiozero import LED
import time


led = LED("BOARD7")

#Assuming the radar is half a mile down the road
distanceToRadar = .5

ser = serial.Serial("/dev/ttyAMA0", baudrate=19200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3.0)

while True:
	rcv = ser.read_until()
	msg = bytearray.fromhex(rcv.hex()).decode()
	if msg != "":
		print(msg)

		#Calculate time in seconds
		timeToIntersection = (distanceToRadar/speed)*3600

		#Output 0 for timeToIntersection (outputting 0 transmits a 1)
		led.off()
		time.sleep(timeToIntersection)
		led.on()
