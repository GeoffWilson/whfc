from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from oslo_config import cfg

app = Flask(__name__)
login_manager = LoginManager()
db = SQLAlchemy()  # Flask-SQLAlchemy extension

flask_opts = [
    cfg.BoolOpt('debug',
                default=False,
                help='Enable debug mode in flask'),
    cfg.BoolOpt('testing',
                default=True,
                help='Enable testing mode in flask'),
    cfg.StrOpt('secret_key',
               default='',
               help='secret key for flask'),
]

# These are the configurations settings for SQLAlchemy
database_opts = [
    cfg.StrOpt('connection_string'),
    cfg.StrOpt('track_modifications')
]


class FlaskConfig(object):
    def __init__(self):
        conf = cfg.CONF
        conf.register_opts(flask_opts, 'flask')
        conf.register_opts(database_opts, 'database')

        for key, value in conf.flask.items():
            setattr(self, key.upper(), value)


def create_app(config_files=None):

    if not config_files:
        config_files = []
    conf = cfg.CONF
    conf(default_config_files=config_files)

    # Flask Config File Configuration
    app.config.from_object(FlaskConfig())

    # Flask-SQLAlchemy configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = conf.database.connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = conf.database.track_modifications

    # Misc Jinja Configuration
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True

    # LoginManager Configuration
    login_manager.init_app(app)
    login_manager._login_disabled = False

    # Set Flask-Login session protection to the highest level
    login_manager.session_protection = 'strong'

    # Initialize the extensions we are using
    db.init_app(app)

    return app
