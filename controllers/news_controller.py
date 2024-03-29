from flask import  jsonify, render_template
from controllers.subjects_controller import getAllSubjects
import requests
from models.envVariables import serviceUrl

def getNews(startNumber,limit):
    try:
        response = requests.get(f'{serviceUrl}/getallnews?startNumber={startNumber}&quantity={limit}')
        return response.json()
    except:
        return {}


def getNewsById(newsId):
    response = requests.get(f'{serviceUrl}/getnews?id={newsId}')
    return response.json()

#retorno dos templates

def home(limit,pageNumber):
    startNumber = (int(limit)*int(pageNumber))-(int(limit)-1)
    noticias = getNews(startNumber,limit)
    assuntos = getAllSubjects()
    return render_template("home.html",newsList=noticias,subjects=assuntos,pageNumber=pageNumber,quantity=limit)

def createNews():
    assuntos = getAllSubjects()
    return render_template("createNewsPost.html",subjects=assuntos)

def editNews(postId):
    noticia = getNewsById(postId)
    assuntos = getAllSubjects()
    return render_template("editNewsPost.html",news=noticia,subjects=assuntos)

def login():
    return render_template("login.html")
