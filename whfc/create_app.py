from flask import Flask
from flask_login import LoginManager
from oslo_config import cfg

app = Flask(__name__)
login_manager = LoginManager()

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


class FlaskConfig(object):
    def __init__(self):
        conf = cfg.CONF
        conf.register_opts(flask_opts, 'flask')

        for key, value in conf.flask.items():
            setattr(self, key.upper(), value)


def create_app(config_files=None):

    if not config_files:
        config_files = []
    conf = cfg.CONF
    conf(default_config_files=config_files)

    # Flask Config File Configuration
    app.config.from_object(FlaskConfig())

    # Misc Jinja Configuration
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True

    # LoginManager Configuration
    login_manager.init_app(app)
    login_manager._login_disabled = False

    return app
