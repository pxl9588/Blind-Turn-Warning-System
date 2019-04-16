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

messages = []

#Only read incoming speeds
messages.append("R+")

#Only read speeds above threshold speed
#messages.append("R0")

#20k samples for up to 139.1 mph
messages.append("S2")

#If we decide to upgrade device firmware
#Flash data so we don't have to keep sending start up commands
#messages.append("A!")

print(messages)

for msg in messages:
	print("sending " + msg)
	for chr in msg:
		ser.write(chr.encode())
		time.sleep(1)
		ser.flush()
