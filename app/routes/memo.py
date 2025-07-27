# routes/auth.py
from flask import Blueprint, request, redirect, url_for, render_template, session, flash
from app.models import Memo, db

memo_bp = Blueprint('memo', __name__)

@memo_bp.route('/memo', methods=['GET', 'POST'])
def memo():
    if request.method == 'POST':
       content = request.form["content"]
       new_msg = Memo(content=content)
       db.session.add(new_msg)
       db.session.commit()

    all_memos = Memo.query.all()
    return render_template("memo.html", memos=all_memos)

@memo_bp.route("/memo/delete/<int:memo_id>", methods=["GET"])
def delete_memo(memo_id):
    memo = Memo.query.get_or_404(memo_id)
    db.session.delete(memo)
    db.session.commit()
    return redirect(url_for("memo.memo"))



