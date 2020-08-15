from flask import Blueprint, redirect, render_template, url_for, request, jsonify, flash
from projectFiles import db
from models import Vister
# from models import Student

home_page = Blueprint('home', __name__, static_folder='static', template_folder='templates')

@home_page.route("/")
@home_page.route("/home")
def index():
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    return render_template("home.html", titel="Akshaha")
