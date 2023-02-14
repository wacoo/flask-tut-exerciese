from flask import Blueprint, render_template

bprint = Blueprint("bprint", __name__, static_folder="static",  template_folder="templates")

@bprint.route("/home")
@bprint.route("/")
def home():
    return render_template("home.html")

@bprint.route("/login")
def login():
    return "Login"