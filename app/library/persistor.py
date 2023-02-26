import random
import numpy
import app.utilities.logger as logger

from PIL import Image

class ErrInvalidInput(Exception):
    pass

log = logger.get_logger(__name__)
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
dir = "images"


def gen_random_id(starts_with="i", length=8, chars=chars):
    return starts_with + ''.join([random.choice(chars) for _ in range(length)])


def persist(canvas, name=None):    
    if not type(canvas) == numpy.ndarray:            
        raise ErrInvalidInput("invalid input type")

    if canvas.shape[0] <= 1 or canvas.shape[1] <= 1:
        raise ErrInvalidInput("invalid canvas size")

    if not name:
        name = gen_random_id()

    log.info(f"persist image name: {name}")

    img = Image.fromarray(canvas, 'RGB')
    img.save(dir + "/" + name + ".png")

    return name

