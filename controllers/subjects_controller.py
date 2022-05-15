from flask import  jsonify, render_template
import requests

baseUrl="http://127.0.0.1:8080"

def getSubjects():
    try:
        response = requests.get(f"{baseUrl}/getallsubjects")
        return response.json()
    except:
        return []

def getSubjectById(id):
    try:
        response = requests.get(f"{baseUrl}/getnewsbyid?id={id}")
        return response.json()
    except:
        return {}

def subjectList():
    assuntos = getSubjects()
    return render_template("subjectslist.html",subjects=assuntos)

def createSubject():
    return render_template("createSubjects.html")

def editSubject(subjectId):
    assunto = getSubjectById(subjectId)
    return render_template("editSubject.html",assunto=assunto)
