from whfc.create_app import create_app

app = create_app(config_files=['/etc/whfc/whfc.conf'])
application = app
