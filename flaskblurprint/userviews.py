from flask import Flask,Blueprint,current_app
from flask import g
u_views = Blueprint("user_views",__name__)


@u_views.route("/index/")
def index():

    return "user views index %s %s" %(g.user_id,g.username)









