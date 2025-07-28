# routes/auth.py
from flask import Blueprint, request, redirect, url_for, render_template, session, flash
from app.models import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)
