from flask import Flask
from amazon.products.views import blueprint
from amazon.settings import ProdConfig

def create_app(config=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(blueprint, url_prefix='/products')