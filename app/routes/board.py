from flask import Blueprint, render_template,request, jsonify
from app.models import db, Message

board_bp = Blueprint('board', __name__)

@board_bp.route("/",methods=["GET", "POST"])
def board():
    if request.method == "POST":
        data = request.get_json()
        new_msg = Message(content=data["content"])
        db.session.add(new_msg)
        db.session.commit()
        return jsonify({"status": "success"}), 201

    messages = Message.query.all()
    return jsonify([{"content": m.content} for m in messages])
    
    


