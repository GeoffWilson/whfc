if __name__ == '__main__':

    from whfc.create_app import create_app

    app = create_app(config_files=['./etc/whfc.conf'])

    # If you use Gevent above please comment out this line!
    app.run('0.0.0.0', port=8080)
