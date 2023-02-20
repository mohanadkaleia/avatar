from app.library import canvas
from app.library import face
from app.library import eyes
from app.library import mouth

c = canvas.Canvas(24, 24)
f = face.Face(c.get())
e = eyes.Eyes(f.get())
m = mouth.Mouth(e.get())

m.draw()
m.show()