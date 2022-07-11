from flask import Flask
from algorithmictradingtier0.ext import site
from algorithmictradingtier0.ext import admin

def create_app():
    """Main Factory"""
    app = Flask(__name__)
    site.init_app(app)
    admin.init_app(app)
    return app

