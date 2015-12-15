import RPi.GPIO as GPIO
import time
import os

BCN3DPlusPath = ('/home/pi/BCN3D_v3_0_2x01.cpp.hex')
BCN3DRPath = ('/home/pi/BCN3DR_v1_1.hex')
BCN3DSigmaPath = ('/home/pi/BCN3D-Updater/Marlin.hex')

#Update the repository
try:
	os.system("cd BCN3D-Updater")
	os.system("git pull")
except:
	pass

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state_24 = GPIO.input(24)
input_state_17 = GPIO.input(17)
input_state_27 = GPIO.input(27)
input_state_22 = GPIO.input(22)
input_state_23 = GPIO.input(23)

def startUp():
#Just a sequence of LEDs to know that the system is running the program
	for x in range(0,4):
	     GPIO.setup(21, GPIO.OUT)
	     GPIO.output(21, GPIO.HIGH)
	     GPIO.setup(13, GPIO.OUT)
	     GPIO.output(13, GPIO.HIGH)
	     time.sleep(0.1)
	     GPIO.output(21, GPIO.LOW)
	     GPIO.output(13, GPIO.LOW)
	     GPIO.setup(20, GPIO.OUT)
	     GPIO.output(20, GPIO.HIGH)
	     GPIO.setup(6, GPIO.OUT)
	     GPIO.output(6, GPIO.HIGH)
	     time.sleep(0.1)
	     GPIO.output(20, GPIO.LOW)
	     GPIO.output(6, GPIO.LOW)
	     GPIO.setup(16, GPIO.OUT)
	     GPIO.output(16, GPIO.HIGH)
	     GPIO.setup(5, GPIO.OUT)
	     GPIO.output(5, GPIO.HIGH)
	     time.sleep(0.1)
	     GPIO.output(16, GPIO.LOW)
	     GPIO.output(5, GPIO.LOW)
	     GPIO.setup(12, GPIO.OUT)
	     GPIO.output(12, GPIO.HIGH)
	     GPIO.setup(11, GPIO.OUT)
	     GPIO.output(11, GPIO.HIGH)
	     time.sleep(0.1)
	     GPIO.output(12, GPIO.LOW)
	     GPIO.output(11, GPIO.LOW)
     	     time.sleep(0.1)

def loadFirmware(firmware):
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM0 -U flash:w:%s -D" % firmware) 
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH) #Status 1
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM1 -U flash:w:%s -D" % firmware) 
	GPIO.setup(20, GPIO.OUT) 
	GPIO.output(20, GPIO.HIGH) #Status 2
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM2 -U flash:w:%s -D" % firmware) 
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH) #Status 3
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM3 -U flash:w:%s -D" % firmware) 
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH) #Status 4
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM4 -U flash:w:%s -D" % firmware) 
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.HIGH) #Status 5
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM5 -U flash:w:%s -D" % firmware) 
	GPIO.setup(6, GPIO.OUT)
	GPIO.output(6, GPIO.HIGH) #Status 6
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM6 -U flash:w:%s -D" % firmware) 
	GPIO.setup(5, GPIO.OUT)
	GPIO.output(5, GPIO.HIGH) #Status 7
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM7 -U flash:w:%s -D" % firmware) 
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH) #Status 8 
	time.sleep(2) #Sleep for 2 seconds
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)	
	GPIO.output(11, GPIO.LOW)

#Main program
def main():
	startUp()
	
	while True:
	  input_state_24 = GPIO.input(24) #Load Button
	  input_state_17 = GPIO.input(17) #Interruptor 1 - BCN3D+
	  input_state_27 = GPIO.input(27) #Interruptor 2 - BCN3DR
	  input_state_22 = GPIO.input(22) #Interruptor 3 - BCN3DSigma
	  input_state_23 = GPIO.input(23) #Interruptor 4 - Unused
	
	  if input_state_24 == False: 
	
			if input_state_17 == False and input_state_27 == True and input_state_22 == True and input_state_23 == True:
				#Interruptor 1 pressed, Loading BCN3D+ firmware
				loadFirmware(BCN3DPlusPath)				
	
			if input_state_27 == False and input_state_17 == True and input_state_22 == True and input_state_23 == True:
				#Interruptor 2 pressed, Loading BCN3DR firmware
				loadFirmware(BCN3DRPath)

			if input_state_22 == False and input_state_27 == True and input_state_17 == True and input_state_23 == True:
				#Interruptor 3 pressed, Loading BCN3DSigma firmware
				loadFirmware(BCN3DSigmaPath)
	
			if input_state_24 == False and input_state_27 == False and input_state_17 == False and input_state_22 == False:
				print 'Rebooting...'
				startUp()
				os.system("sudo reboot")
	
			if input_state_24 == False and input_state_27 == False and input_state_17 == False and input_state_23 == False:
				print 'Powering off the system...'
	                        startUp()
				os.system("sudo poweroff")

#Just the regular boilerplate to start the program
if __name__ == '__main__':
	main()
