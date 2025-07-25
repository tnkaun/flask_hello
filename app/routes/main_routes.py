from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")
	
@main_bp.route("/about")
def about():
    return render_template("about.html")
	
@main_bp.route("/contact")
def contact():
    return render_template("contact.html")
