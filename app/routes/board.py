from flask import Blueprint, render_template,request, jsonify,redirect,url_for
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

@board_bp.route("/board/delete/<int:msg_id>", methods=["POST"])
def delete_msg(msg_id):
    msg = Message.query.get_or_404(msg_id)
    db.session.delete(msg)
    db.session.commit()
    return redirect(url_for("board.board"))