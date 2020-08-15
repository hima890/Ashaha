from flask import Blueprint, redirect, render_template, url_for, request, jsonify, flash
from projectFiles import db, bcrypt, login_manager, logout_user, login_user, login_required, current_user
from projectFiles.loginLogout.utilty import choes, newLink
from models import User, Vister
# from models import Student

loginLogout_page = Blueprint('loginLogout', __name__, static_folder='static', template_folder='templates')


@loginLogout_page.route("/register", methods=["POST", "GET"])
def register():
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()

    if current_user.is_authenticated:
        return redirect(url_for("account.account"))
    if request.method == "POST":
        name = request.form.get("name")
        userName = request.form.get("userName")
        email = request.form.get("email")
        phoneNumber = request.form.get("phoneNumber")

        password = request.form.get("password")
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        gender = request.form.get("gender")
        proFimage = choes(gender)
        proLink = newLink()

        newUser = User(name=name, userName=userName, email=email, phoneNumber=phoneNumber, password=pw_hash, proFimage=proFimage, proLink=proLink, gender=gender)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for('account.account'))
    return render_template("register.html", titel="Register")



@loginLogout_page.route("/login", methods=["POST", "GET"])
def login():
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for("home.index"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remberme = request.form.get("remberme")
        user = User.query.filter_by(email=email).first()
        if user:
            hashPassword = user.password
            check = bcrypt.check_password_hash(hashPassword, password)
            if check:
                login_user(user, remember=True)
                return redirect(url_for('account.account'))
            else:
                login_user(user, remember=False)
                return redirect(url_for('account.account'))
        else:
            flash("كشف للايميل و كلمة السر تاني", "danger")
            return redirect(url_for('loginLogout.login'))
    return render_template("login.html", titel="Login")


@loginLogout_page.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.index", titel="Home"))