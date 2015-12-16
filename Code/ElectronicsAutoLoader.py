#Electronics Auto Loader - Enric Gómez Pitarch & Marc Cobler
#BCN3D Technologies - Fundacio CIM
#
#Python program that can upload the firmware up to 8 boards in series
#It has 4 rocker switches to select the firmware to upload and a load button to
#start the sequence. First it ckecks for internet connection and pulls updates from github.
#It uses avrdude for .hex upload

#PIN Connections
#SWITCH 1		-->		PIN11 - GPIO17
#SWITCH 2		-->		PIN13 - GPIO27
#SWITCH 3		-->		PIN15 - GPIO22
#SWITCH 4		-->		PIN16 - GPIO23
#LOAD BUTTON	-->		PIN18 - GPIO24
#LED1			-->		PIN23 - GPIO11
#LED2			-->		PIN29 - GPIO5
#LED3			-->		PIN31 - GPIO6
#LED4			-->		PIN33 - GPIO13
#LED5			-->		PIN32 - GPIO12
#LED6			-->		PIN36 - GPIO16
#LED7			-->		PIN38 - GPIO20
#LED8			-->		PIN40 - GPIO21

import RPi.GPIO as GPIO
import time
import os
import sys
import socket

repoPath = "/home/pi/arduino-auto-loader"
BCN3DPlusPath = ('/home/pi/arduino-auto-loader/Code/files/BCN3D_v3_0_2x01.hex')
BCN3DRPath = ('/home/pi/arduino-auto-loader/Code/files/BCN3DR_v1_1.hex')
#BCN3DSigmaPath = ('/home/pi/BCN3D-Updater/Marlin.hex')

def haveInternet():
	REMOTE_SERVER = "www.google.com"
	try:
		host = socket.gethostbyname(REMOTE_SERVER)
		s = socket.create_connection((host, 443))
		return True
	except:
		pass
	return False


def syncGithub():
	#Update the repositor
	if haveInternet():
		print "Internet is ON!"
		try:
			print "Getting updates from github"
			os.chdir(repoPath)
			currentDirectory = os.getcwd()
			print "the current directory is: %s" % currentDirectory
			os.system("git pull")
		except:
			print "Something went wrong, check you internet connection"
			pass
	else:
		print "No internet, no github sync"
        

def manageInputs():
        print "Setting the input switches"
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        #Set Pull ups to pins
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #Read the inputs
        input_state_24 = GPIO.input(24)
        input_state_17 = GPIO.input(17)
        input_state_27 = GPIO.input(27)
        input_state_22 = GPIO.input(22)
        input_state_23 = GPIO.input(23)

def startUpLEDS():
	#Just a sequence of LEDs to know that the system is running the program
	#We need root access to manipulate the GPIO!
	print "Lighting some LEDs..."
	for x in range(0,4):
	     GPIO.setup(21, GPIO.OUT)
	     GPIO.output(21, GPIO.HIGH)
	     GPIO.setup(13, GPIO.OUT)
	     GPIO.output(13, GPIO.HIGH)
	     time.sleep(0.1)
	     print "."
	     GPIO.output(21, GPIO.LOW)
	     GPIO.output(13, GPIO.LOW)
	     GPIO.setup(20, GPIO.OUT)
	     GPIO.output(20, GPIO.HIGH)
	     GPIO.setup(6, GPIO.OUT)
	     GPIO.output(6, GPIO.HIGH)
	     time.sleep(0.1)
	     print "."
	     GPIO.output(20, GPIO.LOW)
	     GPIO.output(6, GPIO.LOW)
	     GPIO.setup(16, GPIO.OUT)
	     GPIO.output(16, GPIO.HIGH)
	     GPIO.setup(5, GPIO.OUT)
	     GPIO.output(5, GPIO.HIGH)
	     time.sleep(0.1)
	     print "."
	     GPIO.output(16, GPIO.LOW)
	     GPIO.output(5, GPIO.LOW)
	     GPIO.setup(12, GPIO.OUT)
	     GPIO.output(12, GPIO.HIGH)
	     GPIO.setup(11, GPIO.OUT)
	     GPIO.output(11, GPIO.HIGH)
	     time.sleep(0.1)
	     print "."
	     GPIO.output(12, GPIO.LOW)
	     GPIO.output(11, GPIO.LOW)
     	 time.sleep(0.1)
     	 print "."

def loadFirmware(firmware):
	print "Loading " + str(firmware) + " to port 0" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM0 -U flash:w:%s -D" % firmware) 
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH) #Status 1
	print "Loading " + str(firmware) + " to port 1" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM1 -U flash:w:%s -D" % firmware) 
	GPIO.setup(20, GPIO.OUT) 
	GPIO.output(20, GPIO.HIGH) #Status 2
	print "Loading " + str(firmware) + " to port 2" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM2 -U flash:w:%s -D" % firmware) 
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH) #Status 3
	print "Loading " + str(firmware) + " to port 3" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM3 -U flash:w:%s -D" % firmware) 
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH) #Status 4
	print "Loading " + str(firmware) + " to port 4" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM4 -U flash:w:%s -D" % firmware) 
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(13, GPIO.HIGH) #Status 5
	print "Loading " + str(firmware) + " to port 5" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM5 -U flash:w:%s -D" % firmware) 
	GPIO.setup(6, GPIO.OUT)
	GPIO.output(6, GPIO.HIGH) #Status 6
	print "Loading " + str(firmware) + " to port 6" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM6 -U flash:w:%s -D" % firmware) 
	GPIO.setup(5, GPIO.OUT)
	GPIO.output(5, GPIO.HIGH) #Status 7
	print "Loading " + str(firmware) + " to port 7" 
	os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM7 -U flash:w:%s -D" % firmware) 
	GPIO.setup(11, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH) #Status 8 
	time.sleep(4) #Sleep for 4 seconds
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
	syncGithub()
	manageInputs()
	startUpLEDS()
	#LOOP
	while True:
                try:
                        #Read the status of the switches and buttons
                        #print "Reading the inputs..."
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
                                                
                                #If switches 1,2,3 are selected and the load button pressed --> REBOOT
                                if input_state_24 == False and input_state_27 == False and input_state_17 == False and input_state_22 == False:
                                        print 'Rebooting...'
                                        startUpLEDS()
                                        os.system("sudo reboot")
                                #If switches 1,2,4 are selected and the load button pressed --> SHUTDOWN
                                if input_state_24 == False and input_state_27 == False and input_state_17 == False and input_state_23 == False:
                                        print 'Powering off the system...'
                                        startUpLEDS()
                                        os.system("sudo poweroff")
                except KeyboardInterrupt:
                        print "program closed by user"
                        GPIO.cleanup()
                        sys.exit()
                except:
                        print "Other error or exception ocurred!"
                        GPIO.cleanup()
                        sys.exit()                        

#Just the regular boilerplate to start the program
if __name__ == '__main__':
	print "Starting the Electronics Auto Loader...!"
	main()
