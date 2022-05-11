import os
from flask import Blueprint, current_app

from controllers.news_controller import home as news_home
from controllers.news_controller import createNews as news_create
from controllers.news_controller import editNews as news_edit
from controllers.news_controller import login as login_user

template_dir = os.path.abspath('sitedenoticiasadm/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)

@news_bp.route("/")
def home():
    # if user is logged, else
    return news_home()

@news_bp.route("/create")
def createNews():
    return news_create()

@news_bp.route("/edit/<int:postId>")
def editNews(postId):
    return news_edit(postId)

@news_bp.route("/login")
def login():
    return login_user()
