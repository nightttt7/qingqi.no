from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # register blueprints here

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .Blog import Blog as Blog_blueprint
    app.register_blueprint(Blog_blueprint, url_prefix='/blog')

    from .CV import CV as CV_blueprint
    app.register_blueprint(CV_blueprint, url_prefix='/cv')

    from .timesheet import timesheet as timesheet_blueprint
    app.register_blueprint(timesheet_blueprint, url_prefix='/timesheet')

    from .gameoflife import gameoflife as gameoflife_blueprint
    app.register_blueprint(gameoflife_blueprint, url_prefix='/gameoflife')

    return app
