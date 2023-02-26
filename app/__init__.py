from app import views
from flask import Flask

# Register all views
app = Flask(__name__)
views.register(app)