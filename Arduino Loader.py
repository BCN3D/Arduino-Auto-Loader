import RPi.GPIO as GPIO
import time
import os

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
	
while True:

  input_state_24 = GPIO.input(24)
  input_state_17 = GPIO.input(17)
  input_state_27 = GPIO.input(27)
  input_state_22 = GPIO.input(22)
  input_state_23 = GPIO.input(23)

  if input_state_24 == False: 

		if input_state_17 == False and input_state_27 == True:

			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM0 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(21, GPIO.OUT)
			GPIO.output(21, GPIO.HIGH) #Status 1
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM1 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(20, GPIO.OUT) 
			GPIO.output(20, GPIO.HIGH) #Status 2
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM2 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(16, GPIO.OUT)
			GPIO.output(16, GPIO.HIGH) #Status 3
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM3 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(12, GPIO.OUT)
			GPIO.output(12, GPIO.HIGH) #Status 4
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM4 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(13, GPIO.OUT)
			GPIO.output(13, GPIO.HIGH) #Status 5
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM5 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(6, GPIO.OUT)
			GPIO.output(6, GPIO.HIGH) #Status 6
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM6 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(5, GPIO.OUT)
			GPIO.output(5, GPIO.HIGH) #Status 7
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM7 -U flash:w:BCN3D_v3_0_2x01.cpp.hex -D") 
			GPIO.setup(11, GPIO.OUT)
			GPIO.output(11, GPIO.HIGH) #Status 8 
			time.sleep(2)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(20, GPIO.LOW)
			GPIO.output(16, GPIO.LOW)
			GPIO.output(12, GPIO.LOW)
			GPIO.output(13, GPIO.LOW)
			GPIO.output(6, GPIO.LOW)
			GPIO.output(5, GPIO.LOW)	
			GPIO.output(11, GPIO.LOW)

		if input_state_27 == False and input_state_17 == True:

			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM0 -U flash:w:BCN3DR_v1_1.hex -D") 
			GPIO.setup(21, GPIO.OUT)
			GPIO.output(21, GPIO.HIGH) #Status 1
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM1 -U flash:w:BCN3DR_v1_1.hex -D")  
			GPIO.setup(20, GPIO.OUT) 
			GPIO.output(20, GPIO.HIGH) #Status 2
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM2 -U flash:w:BCN3DR_v1_1.hex -D")  
			GPIO.setup(16, GPIO.OUT)
			GPIO.output(16, GPIO.HIGH) #Status 3
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM3 -U flash:w:BCN3DR_v1_1.hex -D") 
			GPIO.setup(12, GPIO.OUT)
			GPIO.output(12, GPIO.HIGH) #Status 4
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM4 -U flash:w:BCN3DR_v1_1.hex -D")  
			GPIO.setup(13, GPIO.OUT)
			GPIO.output(13, GPIO.HIGH) #Status 5
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM5 -U flash:w:BCN3DR_v1_1.hex -D")  
			GPIO.setup(6, GPIO.OUT)
			GPIO.output(6, GPIO.HIGH) #Status 6
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM6 -U flash:w:BCN3DR_v1_1.hex -D") 
			GPIO.setup(5, GPIO.OUT)
			GPIO.output(5, GPIO.HIGH) #Status 7
			os.system("avrdude -p m2560 -c avrispmkII -V -P/dev/ttyACM7 -U flash:w:BCN3DR_v1_1.hex -D")  
			GPIO.setup(11, GPIO.OUT)
			GPIO.output(11, GPIO.HIGH) #Status 8 
			time.sleep(2)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(20, GPIO.LOW)
			GPIO.output(16, GPIO.LOW)
			GPIO.output(12, GPIO.LOW)
			GPIO.output(13, GPIO.LOW)
			GPIO.output(6, GPIO.LOW)
			GPIO.output(5, GPIO.LOW)	
			GPIO.output(11, GPIO.LOW)

		if input_state_27 == False and input_state_17 == False and input_state_24 == False and input_state_22 == False:
			
			GPIO.setup(21, GPIO.OUT)
                        GPIO.output(21, GPIO.HIGH) #Status 1
			GPIO.setup(13, GPIO.OUT)
                        GPIO.output(13, GPIO.HIGH) #Status 5
                	GPIO.setup(20, GPIO.OUT)
                        GPIO.output(20, GPIO.HIGH) #Status 2
			GPIO.setup(6, GPIO.OUT)
                        GPIO.output(6, GPIO.HIGH) #Status 6
          	  	GPIO.setup(16, GPIO.OUT)
                        GPIO.output(16, GPIO.HIGH) #Status 3
                        GPIO.setup(5, GPIO.OUT)
                        GPIO.output(5, GPIO.HIGH) #Status 7
                	GPIO.setup(12, GPIO.OUT)
                        GPIO.output(12, GPIO.HIGH) #Status 4
                        GPIO.setup(11, GPIO.OUT)
                        GPIO.output(11, GPIO.HIGH) #Status 8
			time.sleep(0.6)
			GPIO.cleanup(21)
			GPIO.cleanup(13)
			GPIO.cleanup(20)
			GPIO.cleanup(6)
			GPIO.cleanup(16)
			GPIO.cleanup(5)
			GPIO.cleanup(12)
			GPIO.cleanup(11)
			os.system("sudo reboot")


		if input_state_27 == False and input_state_17 == False and input_state_24 == False and input_state_23 == False:

                        GPIO.setup(21, GPIO.OUT)
                        GPIO.output(21, GPIO.HIGH) #Status 1
                        GPIO.setup(13, GPIO.OUT)
                        GPIO.output(13, GPIO.HIGH) #Status 5
                        GPIO.setup(20, GPIO.OUT)
                        GPIO.output(20, GPIO.HIGH) #Status 2
                        GPIO.setup(6, GPIO.OUT)
                        GPIO.output(6, GPIO.HIGH) #Status 6
                        GPIO.setup(16, GPIO.OUT)
                        GPIO.output(16, GPIO.HIGH) #Status 3
                        GPIO.setup(5, GPIO.OUT)
                        GPIO.output(5, GPIO.HIGH) #Status 7
                        GPIO.setup(12, GPIO.OUT)
                        GPIO.output(12, GPIO.HIGH) #Status 4
                        GPIO.setup(11, GPIO.OUT)
                        GPIO.output(11, GPIO.HIGH) #Status 8
                        time.sleep(0.6)
                        GPIO.cleanup(21)
                        GPIO.cleanup(13)
                        GPIO.cleanup(20)
                        GPIO.cleanup(6)
                        GPIO.cleanup(16)
                        GPIO.cleanup(5)
                        GPIO.cleanup(12)
                        GPIO.cleanup(11)
			os.system("sudo poweroff")		
		
	

