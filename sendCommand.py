import serial
import time

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate=19200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)


command = input("Enter a command to send: ")

for chr in command:
	ser.write(chr.encode())
	time.sleep(1)
	ser.flush()

