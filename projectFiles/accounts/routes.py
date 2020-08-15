from flask import Blueprint, redirect, render_template, url_for, request, jsonify, flash
from projectFiles import db, bcrypt, login_manager, logout_user, login_user, login_required, current_user
from projectFiles.accounts.utillty import choce
from models import User, Post, Vister
# from models import Student

account_page = Blueprint('account', __name__, static_folder='static', template_folder='templates')


@account_page.route("/account")
@login_required
def account():
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    if current_user.gender == "زول":
        type1 = "men"
    else:
        type1 = "women"
    user = current_user
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.date_created.desc()).all()
    return render_template("account.html", titel="Account", type1=type1, posts=posts)




@account_page.route("/i/<link>", methods=["GET", "POST"])
def messageToAccount(link):
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    user = User.query.filter_by(proLink=link).first()
    if user:
        type1 = user.gender
        if request.method == "POST":
            text = request.form.get("text")
            image = choce()
            newPost = Post(content=text, user_id=user.id, proFimage=choce())
            db.session.add(newPost)
            db.session.commit()
            flash("نشكرك علي الطعمجة", "success")
            return redirect(url_for("account.messageToAccount", titel="Message Account", user=user, type1=type1, link=link))
    else:
        flash("الرابط دا ما تبعنا", "danger")
        return redirect(url_for("home.index", titel="Akshah"))
    return render_template("messageToAccount.html", titel="Message Account", user=user, type1=type1, link=link)




@account_page.route("/contactUs", methods=["GET", "POST"])
def contact():
    link = "71066486de0e11eab9df30d16b4722d4"
    user = User.query.filter_by(proLink=link).first()
    if user:
        type1 = user.gender
        if request.method == "POST":
            text = request.form.get("text")
            image = choce()
            newPost = Post(content=text, user_id=user.id, proFimage=choce())
            db.session.add(newPost)
            db.session.commit()
            flash("نشكرك علي الطعمجة", "success")
            return redirect(url_for("account.contact", titel="Message Account", user=user, type1=type1))
    else:
        flash("الرابط دا ما تبعنا", "danger")
        return redirect(url_for("home.index", titel="Akshah"))
    return render_template("contactUs.html", titel="Contact Us", user=user, type1=type1)


