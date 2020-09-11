from neopixel import *
import numpy as np

class DisplayController:

    def __init__(self, display, height, width):
        self.charDict = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
        self.charNum = {'0','1','2','3','4','5','6','7','8','9'}
        self.charSigns = {'.',',','?','!','@','_','*','#','$','%','&','(',')','+','-','/',':',';','<','=','>','[',']','^','°','{','|','}','na','\'}
        self.offsetChars = [1,1]
        self.offsetNums = [14,1]

        self.display = display
        self.height = height
        self.width = width
        self.displayArray = np.zeros((height, width, 3), dtype=np.uint8)

        self.font_pil = Image.open('font.png') 
        self.font_np = np.array(font_pil)
        self.font_size = [5,3]
        self.font_offset = [1,1]

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
