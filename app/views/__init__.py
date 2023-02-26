from .avatar import bp as avatar_bp

def register(app):
    app.register_blueprint(avatar_bp)    