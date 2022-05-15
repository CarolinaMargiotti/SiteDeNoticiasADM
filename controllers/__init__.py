import os
from flask import Blueprint, current_app,request

from controllers.news_controller import home as news_home
from controllers.news_controller import createNews as news_create
from controllers.news_controller import editNews as news_edit
from controllers.news_controller import login as login_user
from controllers.news_controller import subjectList as subject_list
from controllers.news_controller import createSubject as create_subject

template_dir = os.path.abspath('sitedenoticiasadm/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)

@news_bp.route("/")
def home():
    req = request.args
    startNumber = req.get("startNumber",1)
    limit = req.get("limit",10)

    # if user is logged, else
    return news_home(startNumber,limit)

@news_bp.route("/create")
def createNews():
    return news_create()

@news_bp.route("/edit/<int:postId>")
def editNews(postId):
    return news_edit(postId)

@news_bp.route("/login")
def login():
    return login_user()

@news_bp.route("/subjectslist")
def subjectList():
    return subject_list()

@news_bp.route("/createsubject")
def createSubject():
    return create_subject()