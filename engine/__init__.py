from flask import Flask, redirect, url_for
import csv

pytaniaRaw = open('./engine/base/pytania.csv', 'r', newline='')
pytania = csv.DictReader(pytaniaRaw, delimiter=";", quotechar='"')

catAM = []
catA1 = []
catA2 = []
catA = []
catB1 = []
catB = []
catE = []
catC = []
catC1 = []
catD = []
catD1 = []
catT = []

def create_app():
    app = Flask(__name__)

    getQuestionsCategories()

    from .home import home
    from .questions import questions
    from .media import media

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(questions, url_prefix='/question/')
    app.register_blueprint(media, url_prefix='/media/')
    

    return app

def getQuestionsCategories():
    global catAM, catA1, catA2, catA, catB1, catB, catE, catC, catC1, catD, catD1catT 
    pytaniaRaw.seek(0)

    for row in pytania:
        if(row['Kategorie'] == "AM"):
            catAM.append(row['Lp.'])
        if(row['Kategorie'] == "A1"):
            catA1.append(row['Lp.'])
        if(row['Kategorie'] == "A2"):
            catA2.append(row['Lp.'])
        if(row['Kategorie'] == "A"):
            catA.append(row['Lp.'])
        if(row['Kategorie'] == "B1"):
            catB1.append(row['Lp.'])
        if(row['Kategorie'] == "B"):
            catB.append(row['Lp.'])
        if(row['Kategorie'] == "E"):
            catE.append(row['Lp.'])
        if(row['Kategorie'] == "C"):
            catC.append(row['Lp.'])
        if(row['Kategorie'] == "C1"):
            catC1.append(row['Lp.'])
        if(row['Kategorie'] == "D"):
            catD.append(row['Lp.'])
        if(row['Kategorie'] == "D1"):
            catD1.append(row['Lp.'])
        if(row['Kategorie'] == "T"):
            catT.append(row['Lp.'])

    pytaniaRaw.seek(0)




def getQuestion(number):
    for row in pytania:
        if row['Lp.'] == number:
            pytaniaRaw.seek(0)
            return row

    return {'Lp.': '0', 
            'Numer pytania': '0', 
            'Pytanie': '', 
            'Odpowiedź A': '', 
            'Odpowiedź B': '', 
            'Odpowiedź C': '', 
            'Poprawna odp': 'A', 
            'Media': '', 
            'Kategorie': ''}