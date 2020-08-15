from flask import Blueprint, redirect, render_template, url_for, request, jsonify, flash
from projectFiles import db
from projectFiles.admin.utilits import count1, count2, cont3, cont4
from flask import jsonify
from models import Post, User
# from models import Student

admin_page = Blueprint('admin', __name__, static_folder='static', template_folder='templates')

@admin_page.route("/admin")
def admin():
    posts = Post.query.order_by(Post.date_created.desc()).limit(5).all()
    adminPost = Post.query.filter_by(user_id=2).limit(5).all()
    users = cont3()
    ip = cont4()
    post = Post
    return render_template("admin.html", titel="Admin", posts=posts, users=users, post2=post, vister=ip, adminPost=adminPost)

@admin_page.route("/datapass")
def data():
    mens = count1()
    womens = count2()
    return jsonify(mens = mens, womens = womens )



@admin_page.route("/searsh", methods=["POST", "GET"])
def searsh():
    if request.method == "POST":
        query = request.form.get("searsh")
        user = User.query.filter_by(name=query).first()
        if user:
            if user.gender == "زول":
                type1 = "men"
            else:
                type1 = "women"
            return render_template("searsh.html", titel="Account", type1=type1, user=user)

        else:
            user = User.query.filter_by(phoneNumber=query).first()
            if user.gender == "زول":
                type1 = "men"
            else:
                type1 = "women"
            return render_template("searsh.html", titel="Account", type1=type1, user=user)



