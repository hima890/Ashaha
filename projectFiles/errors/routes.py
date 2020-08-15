from flask import Blueprint, render_template, request
from models import Vister

errors = Blueprint('errors', __name__,
template_folder="templates",
static_folder="static")


@errors.app_errorhandler(404)
def error_404(error):
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    return render_template('404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    return render_template('403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    ip = request.remote_addr
    vister = Vister.query.filter_by(ip=ip).first()
    if vister:
        pass
    else:
        newVister = Vister(ip=ip)
        db.session.add(newVister)
        db.session.commit()
    return render_template('500.html'), 500