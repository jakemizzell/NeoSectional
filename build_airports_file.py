#build_airports_file.py
#This script will cycle through the airport identifiers located in the airports file and light up the appropriate LED
#allowing for editing the airport identifier, or by pressing Enter accepting the current airport identifier.
#once all the airports have been looked at, the file is written building a new airports file.
#Be sure to edit the LED_COUNT to match the number of leds used.
#Also, be sure to edit the LED_STRIP to match the GRB or RGB arrangement of the led strip you are using.

import urllib2
import time
from neopixel import *
import sys

# LED strip configuration:
LED_COUNT      = 70      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_RGB   # Strip type and colour ordering

#misc variables
color = Color(255,255,255)
black_color = Color(0,0,0)
filename = "/NeoSectional/airports" #change name to airports when done debugging, or rename the file to airports when ready

#functions
def neo(strip, i, color, wait_ms=50):
	"""light up one pixel."""
	strip.setPixelColor(i, color)
	strip.show()
	#time.sleep(wait_ms/1000.0)

#main portion of script
if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	strip.begin()

	print ("Build Airports File Script -- Press Ctrl-C to quit.")
	i = 0

	#read airports file
	with open(filename) as f:
    		airports = f.readlines()
	airports = [x.strip() for x in airports]

	#cycle through each LED and set new or accept original airport id
	while i < LED_COUNT:

		airportcode = airports[i]
		neo(strip, i, color) #Light up 1 LED
		print ("LED Num = " + str(i) + ", Airport ID Currently is " + airportcode)
		airport_id = raw_input("    Enter New Identifier (or Enter to Accept Current ID): ")

		if airport_id == "":
			pass
		elif airport_id == airportcode:
			pass
		else:
			airports[i] = airport_id.upper() #change input to uppercase if necessary

		print ("    LED number = " + str(i) + ", Identifier = " + airports[i])
		print ("")
		i = i + 1
		neo(strip, i-1, black_color) #turn off current LED before turning on the next one

	#write new airports file
	f= open(filename,"w+")
	for airportcode in airports:
		f.write(airportcode + "\r\n")
	f.close()
