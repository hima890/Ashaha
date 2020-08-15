from flask import Blueprint, redirect, render_template, url_for, request, jsonify, flash
from projectFiles import db, bcrypt, login_manager, logout_user, login_user, login_required, current_user
from models import User, Vister
from projectFiles.resetPassword.utilty import send_reset_email

# from models import Student

reset_page = Blueprint('reset', __name__, static_folder='static', template_folder='templates')


@reset_page.route("/resetPassword", methods=["POST", "GET"])
def reset_request():
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    if request.method == "POST":
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        send_reset_email(user)
        flash('رسلنا ليك في ايميل امشي كشف له', 'info')
        return redirect(url_for('loginLogout.login'))
    return render_template('reset_request.html', title='Reset Password')
    




@reset_page.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('رمز تفعيل غير صالح', 'warning')
        return redirect(url_for('reaet.reset_request'))
    
    if request.method == "POST":
        password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('غيرنا كلمة السر سجل دخولك عادي', 'success')
        return redirect(url_for('loginLogout.login'))
    return render_template('reset_token.html', title='Reset Password', token=token)