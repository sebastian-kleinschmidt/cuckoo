from neopixel import *
import numpy as np

class DisplayController:

    def __init__(self, display, height, width):
        self.display = display
        self.height = height
        self.width = width
        self.displayArray = np.zeros((height, width, 3), dtype=np.uint8)

    def setPixel(self,x,y,color):
        self.displayArray[x,y] = color
        return True

    def setIcon(self,icon):
        print(icon.shape)
        for x in range(icon.shape[0]):
            for y in range(icon.shape[1]):
                self.displayArray[x,y,0] = icon[x,y,1]
                self.displayArray[x,y,1] = icon[x,y,0]
                self.displayArray[x,y,2] = icon[x,y,2]
        return True

    def updateScreen(self):
        for y in range(self.width):
            for x in range(self.height):
                print(x+y*self.height)
                print(self.displayArray[x,y,2])
                self.display.setPixelColor(x+y*self.height, Color(int(self.displayArray[x,y,0]),int(self.displayArray[x,y,1]),int(self.displayArray[x,y,2])))
	self.display.show()
        return True

    def clearScreen(self):
	print('Shutdown Display...')
        for i in range(self.height*self.width):
            self.display.setPixelColor(i, Color(0, 0, 0))
        self.display.show()
        return True
