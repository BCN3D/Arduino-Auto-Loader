# Arduino Auto Loader
Here at **BCN3DTechnologies**, all of our 3D Printers are shipped with an Arduino on its heart. So obviously, we need to load the firmware to a bunch of microcontrollers. That's a tedious work to do because it takes us about 1,5 min to load a single firmware with the Arduino IDE. Compile, Load, Verify and Repeat.
If you take that time and multiply it by the number of printers we sell in a month, it's a lot of time wasted for the person in front of the computer. So we decided to make something about it.

##How it works
It couldn't be easier. Using a Raspberry Pi as a single board computer, we attached a 10 port USB hub and then plug in the Arduinos using an extension cable. The Raspberry detects the Arduinos and it uploads the code to the arduinos sequentially using *avrdude* commands.
Of course, as we carry different 3D printers, we have toggle switches to be able to select the correct firmware and a LED to every Arduino indicating if everything went well.
Then all the electronics are packaged in a 3D printed enclosure of course!
##Bill of materials
The list of things you'll need to replicate this project:
* 1x Raspberry Pi. We've used a Model A+ but any will fit. 
* 1x 5V power supply
* 8x USB Extension cable. about 20 cm long.
* 8x green LEDs with their current limiting resistor (330 Ohms)
* A couple of meters of 22AWG wire of different colors.
* 4 toggle switches. We used power supply ones.
* 2 push buttons
* Acces to a 3D Printer

Optionally we've included a wifi dongle to access the raspberry via SSH if needed to do some maintenance.
The total cost of the project is about 50€ including the raspberry.

##Code
The code is made in Python and you can download from the repository. We've configured the raspberry in order to run the script just after the powerup. You can follow [this instructions](http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/auto-running-programs) to do that.
You'll also need to configure the raspberry to start without login like [here](http://stackoverflow.com/questions/17830333/start-raspberry-pi-without-login).
If you want to do some wireless maintenance you'll need to configure the ssh server too. This is [how it's done](https://www.raspberrypi.org/documentation/remote-access/ssh/).

##Printed Parts
You can download all the **STL** files if you want to print our design or make your own.
The files are: 
* Box.stl
* Top Box.stl
* USB Fixer.stl


##Milestones
We've managed to improve the way we load the firmware to our electronics. It will serve to our future electronics as well. 

Now we can load a 120KB firmware to an arduino in 16 seconds. So in the time we upload a firmware to an Arduino with the original IDE we can upload 8! 

It's also a self working system and there's no need of a person looking after it.





