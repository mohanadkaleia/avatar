import numpy
from PIL import Image

class ErrInvalidSize(Exception):
    pass

class Canvas:

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ErrInvalidSize

        self._canvas = numpy.zeros([width, height, 3], dtype=numpy.uint8)

    def get(self):
        return self._canvas

    def show(self):
        im = Image.fromarray(self._canvas)
        im.show()
    