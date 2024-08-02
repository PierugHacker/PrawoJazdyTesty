from flask import Blueprint, render_template, request, url_for, redirect
from . import *
import random

questions = Blueprint('question', __name__)

@questions.route('/id/<qId>')
def question(qId):
    question = getQuestion(qId)
    correctAnswer = 0
    yesNoQuestion = 0

    if question['Poprawna odp'] == 'A':
        correctAnswer = 0
    elif question['Poprawna odp'] == 'B':
        correctAnswer = 1
    elif question['Poprawna odp'] == 'C':
        correctAnswer = 2

    if question['Poprawna odp'] == 'Tak':
        correctAnswer = 0
        yesNoQuestion = 1
    if question['Poprawna odp'] == 'Nie':
        correctAnswer = 1
        yesNoQuestion = 1

    return render_template("question.html", 
                           questionText=question['Pytanie'],
                           yesNoQuestion=yesNoQuestion,
                           answerA=question['Odpowiedź A'],
                           answerB=question['Odpowiedź B'],
                           answerC=question['Odpowiedź C'],
                           media=question['Media'],
                           questionNumber=question['Lp.'],
                           correctAnswer=correctAnswer)

@questions.route('/category/<categoryId>/')
def category(categoryId):
    if categoryId == 'AM':
        return redirect(url_for('question.question', qId='/' + catAM[random.randint(0, len(catAM))]))
    if categoryId == 'A1':
        return redirect(url_for('question.question', qId='/' + catA1[random.randint(0, len(catA1))]))
    if categoryId == 'A2':
        return redirect(url_for('question.question', qId='/' + catA2[random.randint(0, len(catA2))]))
    if categoryId == 'A':
        return redirect(url_for('question.question', qId='/' + catA[random.randint(0, len(catA))]))
    if categoryId == 'B1':
        return redirect(url_for('question.question', qId='/' + catB1[random.randint(0, len(catB1))]))
    if categoryId == 'B':
        return redirect(url_for('question.question', qId='/' + catB[random.randint(0, len(catB))]))
    if categoryId == 'B+E':
        if random.randint(0, 1):
            return redirect(url_for('question.question', qId='/' + catB[random.randint(0, len(catB))]))
        else:
            return redirect(url_for('question.question', qId='/' + catE[random.randint(0, len(catE))]))
    if categoryId == 'C':
        return redirect(url_for('question.question', qId='/' + catC[random.randint(0, len(catC))]))
    if categoryId == 'C1':
        return redirect(url_for('question.question', qId='/' + catC1[random.randint(0, len(catC1))]))
    if categoryId == 'C1+E':
        if random.randint(0, 1):
            return redirect(url_for('question.question', qId='/' + catC1[random.randint(0, len(catC1))]))
        else:
            return redirect(url_for('question.question', qId='/' + catE[random.randint(0, len(catE))]))
    if categoryId == 'C+E':
        if random.randint(0, 1):
            return redirect(url_for('question.question', qId='/' + catC[random.randint(0, len(catC))]))
        else:
            return redirect(url_for('question.question', qId='/' + catE[random.randint(0, len(catE))]))
    if categoryId == 'D':
        return redirect(url_for('question.question', qId='/' + catD[random.randint(0, len(catD))]))
    if categoryId == 'D1':
        return redirect(url_for('question.question', qId='/' + catD1[random.randint(0, len(catD1))]))
    if categoryId == 'D1+E':
        if random.randint(0, 1):
            return redirect(url_for('question.question', qId='/' + catD1[random.randint(0, len(catD1))]))
        else:
            return redirect(url_for('question.question', qId='/' + catE[random.randint(0, len(catE))]))
    if categoryId == 'D+E':
        if random.randint(0, 1):
            return redirect(url_for('question.question', qId='/' + catD[random.randint(0, len(catD))]))
        else:
            return redirect(url_for('question.question', qId='/' + catE[random.randint(0, len(catE))]))
    if categoryId == 'T':
        return redirect(url_for('question.question', qId='/' + catT[random.randint(0, len(catT))]))