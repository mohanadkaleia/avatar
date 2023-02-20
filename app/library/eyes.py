import numpy
from PIL import Image

class ErrInvalidInput(Exception):
    pass


class Eyes:   
    
    def __init__(self, canvas):        
        if not type(canvas) == numpy.ndarray:            
            raise ErrInvalidInput("invalid input type")

        if canvas.shape[0] <= 1 or canvas.shape[1] <= 1:
            raise ErrInvalidInput("invalid canvas size")

        self._canvas = canvas
        self._width = canvas.shape[0]
        self._height = canvas.shape[1]


    def draw(self):                
        margin = 10

        self._canvas[margin][margin] = (100, 100, 100)
        self._canvas[margin][self._width - margin] = (100, 100, 100)
        

    def get(self):
        self.draw()
        return self._canvas

    def show(self):        
        im = Image.fromarray(self._canvas)
        im.show()
        

