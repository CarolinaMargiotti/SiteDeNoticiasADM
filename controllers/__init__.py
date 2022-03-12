import os
from flask import Blueprint, current_app

from controllers.news_controller import home as news_home

template_dir = os.path.abspath('sitedenoticiasadm/templates/')

news_bp = Blueprint("news",__name__,template_folder=template_dir)

@news_bp.route("/")
def home():
    return news_home()