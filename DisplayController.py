import numpy as np

class DisplayController:

    def __init__(self, display, height, width):
        self.display = display
        self.displayArray = np.ones((height, width))*Color(0,0,0)

    def setPixel(x,y,color):
        self.displayArray[x,y] = color
        return True

    def setIcon(icon,col):
        return True

    def updateScreen():
        for y in range(height):
            for x in range(width):
                self.display.setPixelColor(y*width+x, self.displayArray[x,y])
        return True

    def clearScreen():
        for i in range(height, width):
            self.display.setPixelColor(i, Color(0, 0, 0))
        self.display.show()
        return True