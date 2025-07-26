from flask import Blueprint, render_template,request, jsonify
from app.models import Message
from app.extensions import db

board_bp = Blueprint('board', __name__)

@board_bp.route("/board",methods=["GET", "POST"])
def board():
    if request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        new_msg = Message(name=name, content=content)
        db.session.add(new_msg)
        db.session.commit()

    all_msgs = Message.query.all()
    return render_template("board.html", messages=all_msgs)
