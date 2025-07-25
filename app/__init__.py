from flask import Flask
from app.routes.home import home_bp
from app.routes.about import about_bp
from app.routes.contact import contact_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    return app