from neopixel import *
import numpy as np

class DisplayController:

    def __init__(self, display, height, width):
        self.display = display
        self.height = height
        self.width = width
        self.displayArray = np.ones((height, width))*Color(0,0,0)

    def setPixel(self,x,y,color):
        self.displayArray[x,y] = color
        return True

    def setIcon(self,icon):
        return True

    def updateScreen(self):
        for y in range(height):
            for x in range(width):
                self.display.setPixelColor(y*width+x, self.displayArray[x,y])
        return True

    def clearScreen(self):
	print('Shutdown Display...')
        for i in range(self.height*self.width):
            self.display.setPixelColor(i, Color(0, 0, 0))
        self.display.show()
        return True
