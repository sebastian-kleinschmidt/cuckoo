#!/usr/bin/env python3
# Direct port of the Arduino NeoPixel library strandtest example. Showcases
# various animations on a strip of NeoPixels.
 
import time
from neopixel import *
import argparse
import DisplayController
 
# LED strip configuration:
LED_HEIGHT = 8
LED_WIDTH = 32
LED_COUNT = LED_HEIGHT*LED_WIDTH  # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10 # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0 # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Main program logic follows:
if __name__ == '__main__':
 # Process arguments
 parser = argparse.ArgumentParser()
 parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
 args = parser.parse_args()
 
 strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
 strip.begin()
 
 print ('Press Ctrl-C to quit.')
 if not args.clear:
  print('Use "-c" argument to clear LEDs on exit')

 #Initialize Display Controller 
 displayController = DisplayController(strip, LED_HEIGHT, LED_WIDTH)

 # Initialize Plugins
 plugins = []
 plugins.append('Plugin1')
 plugins.append('Plugin2')

 #Logo 8x8
 #Content 8x24

 try:
  while True:
   for j in range(155):
    for i in range(LED_COUNT):
     strip.setPixelColor(i, Color(i, i, i))
    strip.show()
#    time.sleep(100)
 
 except KeyboardInterrupt:
  displayController.clearScreen()
