from flask import request, jsonify, render_template


noticias = [
{'id':0,'titulo':"porquinhos da india",'assunto':"pets",'conteudo':"cuicuicuicuicui"},
{'id':1,'titulo':"cobrinha",'assunto':"pets",'conteudo':"ssssssssssssss"},
{'id':2,'titulo':"macaco",'assunto':"pets",'conteudo':"uh uh uh uh"},
{'id':3,'titulo':'art nouvelle','assunto':'arte','conteudo':'arte dos elfos'},
{'id':4,'titulo':'arte barroca','assunto':'arte','conteudo':'materia da escola'},
{'id':5,'titulo':'lançamento elden ring','assunto':'geek','conteudo':'é um jogo que lançou'},
{'id':6,'titulo':'sonic é bom','assunto':'geek','conteudo':'gotta go fast'},
]

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