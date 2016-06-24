from flask import render_template

from whfc.create_app import app


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')
