import numpy
from PIL import Image

class ErrInvalidInput(Exception):
    pass


class Mouth:    
    
    def __init__(self, canvas):        
        if not type(canvas) == numpy.ndarray:            
            raise ErrInvalidInput("invalid input type")

        if canvas.shape[0] <= 1 or canvas.shape[1] <= 1:
            raise ErrInvalidInput("invalid canvas size")

        self._canvas = canvas
        self._width = canvas.shape[0]
        self._height = canvas.shape[1]


    def draw(self):                
        vmargin = 10
        hmargin = 15

        for j in range(vmargin, self._width - vmargin + 1):            
            self._canvas[hmargin][j] = (100, 0, 255)

    def get(self):
        self.draw()
        return self._canvas

    def show(self):
        im = Image.fromarray(self._canvas)
        im.show()
        

