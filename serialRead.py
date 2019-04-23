import curses
import serial
import gpiozero
import time
import threading
import queue

debug = 1

led = gpiozero.LED("BOARD7")
ser = serial.Serial("/dev/ttyAMA0", baudrate=19200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=3.0)


#Assuming the radar is half a mile down the road
distanceToRadar = .0005

def carPassed(window):
	#For debugging only
        if debug:
                window.addstr(2, 0, "Car passed")
                window.clrtoeol()

	#Turns the LED on to stop transmitting the warning
	led.on()

#Function for anything that needs to be done for setup
def init():
	led.on()

def main(window):
	init()
	deltaTime = 0
	oldTimeToIntersection = 0
	while True:
		rcv = ser.read_until()
		speed = bytearray.fromhex(rcv.hex()).decode().strip()

		#Only perform calculations if real speeds are being read
		if speed != "":

			#Calculate time to intersection
			timeToIntersection = (distanceToRadar/float(speed))*3600

			#If new time to intersection is longer update time to intersection
			if timeToIntersection > oldTimeToIntersection - deltaTime:
				oldTimeToIntersection = timeToIntersection

				#For debugging only
				if debug:
                                        window.addstr(0, 0, "Car will be at intersection in : {0} seconds".format(timeToIntersection))
                                        window.clrtoeol()

				#Start the timer
				startTime = time.clock()

				#Turn led off to transmit 1
				led.off()

			#Calculate time since timer started
			deltaTime = time.clock() - startTime

			#For debugging only
			if debug:
                                window.addstr(1, 0, "timePassed: {0} seconds".format(deltaTime))
                                window.clrtoeol()

			#Check if the time passed exceeds the expected time
			if deltaTime >= oldTimeToIntersection:
				carPassed(window)

			#For debugging only
			if debug:
                                window.refresh()


curses.wrapper(main)
