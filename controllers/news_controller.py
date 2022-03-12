from flask import request, jsonify, render_template

#retorno dos templates
def home():
    return render_template("home.html")