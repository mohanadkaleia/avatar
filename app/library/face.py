import numpy
from PIL import Image

class ErrInvalidInput(Exception):
    pass


class Face:    
    
    def __init__(self, canvas):        
        if not type(canvas) == numpy.ndarray:            
            raise ErrInvalidInput("invalid input type")

        if canvas.shape[0] <= 1 or canvas.shape[1] <= 1:
            raise ErrInvalidInput("invalid canvas size")

        self._canvas = canvas
        self._width = canvas.shape[0]
        self._height = canvas.shape[1]


    def draw(self):                
        margin = 5

        for i in range(margin, self._height - 5):            
            self._canvas[i][margin] = (255, 255, 255)

        for i in range(margin, self._height - 5 + 1):            
            self._canvas[i][self._width - margin] = (255, 255, 255)

        for i in range(margin, self._width - 5):            
            self._canvas[margin][i] = (255, 255, 255)

        for i in range(margin, self._width - 5 + 1):            
            self._canvas[self._height - margin][i] = (255, 255, 255)

    def get(self):
        self.draw()
        return self._canvas

    def show(self):
        im = Image.fromarray(self._canvas)
        im.show()
        

