from flask import Blueprint, render_template, session, redirect, url_for
from flask_socketio import emit
from app import socketio

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("chat.html", username=session.get("username", "匿名"))

@socketio.on("message")
def handle_message(msg):
    user = session.get("username", "匿名")
    emit("message", {"user": user, "msg": msg}, broadcast=True)
