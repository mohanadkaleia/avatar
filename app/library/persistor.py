from PIL import Image


def persist(canvas, name):
    img = Image.fromarray(canvas, 'RGB')
    img.save(name)

