from serial.tools import list_ports
from clint.textui import colored
def main():
	print "Hello there!"
	#getting the comports
	ports=list_ports.comports()
	print ports
	print "There are %d available comports: " % len(ports)
	#list the comports available
	for port in ports:
		print (colored.red(port[0]))



if __name__ == '__main__':
  main()
