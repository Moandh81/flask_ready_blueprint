from flask_sqlalchemy import SQLAlchemy
from myblog.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    from flask import Flask

    app= Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    from .posts.views import post_blueprint
    app.register_blueprint(post_blueprint)
    db.init_app ( app )
    return app
