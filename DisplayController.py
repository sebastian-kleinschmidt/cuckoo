from neopixel import *
import numpy as np

class DisplayController:

    def __init__(self, display, height, width):
        self.display = display
        self.height = height
        self.width = width
        self.displayArray = np.ones((height, width, 3), dtype=int)*100

    def setPixel(self,x,y,color):
        self.displayArray[x,y] = color
        return True

    def setIcon(self,icon):
        return True

    def updateScreen(self):
        for y in range(self.width):
            for x in range(self.height):
                self.display.setPixelColor(x*self.width+y, Color(self.displayArray[x,y,0],self.displayArray[x,y,1],self.displayArray[x,y,2]))
	self.display.show()
        return True

    def clearScreen(self):
	print('Shutdown Display...')
        for i in range(self.height*self.width):
            self.display.setPixelColor(i, Color(0, 0, 0))
        self.display.show()
        return True
