from flask import Flask
from bprint import bprint
app = Flask(__name__)
app.register_blueprint(bprint, url_prefix="/wac")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)