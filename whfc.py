from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5959, debug=True)
