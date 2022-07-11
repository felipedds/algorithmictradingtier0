from algorithmictradingtier0.ext.admin.main import bp

def init_app(app):
    app.register_blueprint(bp)