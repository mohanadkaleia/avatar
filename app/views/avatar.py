import app.utilities.logger as logger

from flask import Blueprint
from app.library import canvas
from app.library import face
from app.library import eyes
from app.library import mouth
from app.library import persistor
from PIL import Image

bp = Blueprint("avatar", __name__)
log = logger.get_logger(__name__)

@bp.route("/")
def home():
    log.info("request /")
    return "wip - something cool is coming up 👻"


@bp.route("/generate")
def generate():  
    log.info("request /generate")

    c = canvas.Canvas(24, 24)
    f = face.Face(c.get())
    e = eyes.Eyes(f.get())
    m = mouth.Mouth(e.get())
    
    name = persistor.persist(m.get())    
    return name + " avatar is generated"


@bp.errorhandler(404)
def page_not_found(error):
    return "oops.. page not found 😝"