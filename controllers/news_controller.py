from flask import request, jsonify, render_template
from models.news import news as noticias

assuntos = ['pets','arte','geek']

def getNews():
    return noticias

def getSubjects():
    return assuntos

#retorno dos templates

def home():
    noticias = getNews()
    return render_template("home.html",newsList=noticias)

def createNews():
    assuntos = getSubjects()
    return render_template("createNewsPost.html",subjects=assuntos)

def editNews(postId):
    noticia = getNews()[postId]
    assuntos = getSubjects()
    return render_template("editNewsPost.html",news=noticia,subjects=assuntos)

def login():
    return render_template("login.html")
