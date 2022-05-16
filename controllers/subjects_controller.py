from flask import  jsonify, render_template
import requests

baseUrl="http://127.0.0.1:8080"

def getSubjects(startNumber,limit):
    try:
        response = requests.get(f"{baseUrl}/getsubjects?startNumber={startNumber}&quantity={limit}")
        return response.json()
    except:
        return []

def getAllSubjects():
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

def subjectList(limit,pageNumber):
    startNumber = (int(limit)*int(pageNumber))-(int(limit)-1)
    assuntos = getSubjects(startNumber,limit)

    return render_template("subjectslist.html",subjects=assuntos,pageNumber=pageNumber,quantity=limit)

def createSubject():
    return render_template("createSubjects.html")

def editSubject(subjectId):
    assunto = getSubjectById(subjectId)
    return render_template("editSubject.html",assunto=assunto)
