from flask import  jsonify, render_template
from controllers.subjects_controller import getSubjects
import requests

baseUrl="http://127.0.0.1:8080"

def getNews(startNumber,limit):
    response = requests.get(f'{baseUrl}/getallnews?startNumber={startNumber}&quantity={limit}')
    return response.json()


def getNewsById(newsId):
    response = requests.get(f'{baseUrl}/getnews?id={newsId}')
    return response.json()

#retorno dos templates

def home(startNumber,limit):
    noticias = getNews(startNumber,limit)
    assuntos = getSubjects()
    return render_template("home.html",newsList=noticias,subjects=assuntos)

def createNews():
    assuntos = getSubjects()
    return render_template("createNewsPost.html",subjects=assuntos)

def editNews(postId):
    noticia = getNewsById(postId)
    assuntos = getSubjects()
    return render_template("editNewsPost.html",news=noticia,subjects=assuntos)

def login():
    return render_template("login.html")
