from flask import  jsonify, render_template
import requests
from models.envVariables import serviceUrl

def getSubjects(startNumber,limit):
    try:
        response = requests.get(f"{serviceUrl}/getsubjects?startNumber={startNumber}&quantity={limit}")
        return response.json()
    except:
        return []

def getAllSubjects():
    try:
        response = requests.get(f"{serviceUrl}/getallsubjects")
        return response.json()
    except:
        return []

def getSubjectById(id):
    try:
        response = requests.get(f"{serviceUrl}/getnewsbyid?id={id}")
        return response.json()
    except:
        return {}

def subjectList(limit,pageNumber):
    startNumber = (int(limit)*int(pageNumber))-(int(limit)-1)
    assuntos = getSubjects(startNumber,limit)

    return render_template("subjectslist.html",subjects=assuntos,pageNumber=pageNumber,quantity=limit)

def createSubject():
    return render_template("createSubjects.html")

def editSubject(subjectId):
    assunto = getSubjectById(subjectId)
    return render_template("editSubject.html",assunto=assunto)
