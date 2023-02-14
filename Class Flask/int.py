from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<uname>")
def profile(uname):
    return '{}\'s profile'.format(escape(uname))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', uname='Wondmagegn Abriham'))
