from flask import Blueprint, render_template,request, jsonify
from app.models import db, Message

home_bp = Blueprint('home', __name__)

@home_bp.route("/",methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        new_msg = Message(name=data["name"], content=data["content"])
        db.session.add(new_msg)
        db.session.commit()
        return jsonify({"status": "success"}), 201

    messages = Message.query.all()
    return jsonify([{"name": m.name, "content": m.content} for m in messages])
    
    
    
    
    
    #return render_template("index.html")


