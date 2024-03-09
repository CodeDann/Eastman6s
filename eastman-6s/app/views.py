from flask import render_template, request, session, redirect, url_for
from app import app

from . import db, models
from .forms import *
from .models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    # handle all posts
    if request.method == 'POST':
        if 'start' in request.form:
            return redirect(url_for('q1'))
        elif 'info' in request.form:
            return redirect(url_for('moreinfo'))

    return render_template('index.html', title='Homepage')


@app.route('/Question1', methods=['GET', 'POST'])
def q1():
    # debugging block
    print("---VALUES---")
    for key in session:
        print(key, session[key])
    # end debugging block
    if request.method == 'POST':
        if 'good' in request.form:
            return redirect(url_for('restore'))
        elif 'bad' in request.form:
            return redirect(url_for('extract'))
        elif 'uncertain' in request.form:
            session['q1'] = 'uncertain'
            return redirect(url_for('q2'))

    return render_template('prognosis.html', title='Question 1')


@app.route('/Question2', methods=['GET', 'POST'])
def q2():
    # debugging block
    print("---VALUES---")
    for key in session:
        print(key, session[key])
    # end debugging block

    if request.method == 'POST':
        if 'absent' in request.form:
            session['q2'] = 'absent'
            return redirect(url_for('q3'))
        elif 'present' in request.form:
            session['q2'] = 'present'
            return redirect(url_for('q3'))

    return render_template('3rdMolar.html', title='Question 2')


@app.route('/Question3', methods=['GET', 'POST'])
def q3():
    # debugging block
    print("---VALUES---")
    for key in session:
        print(key, session[key])
    # end debugging block

    if 'upper' in request.form:
        session['q3'] = 'upper'
        return redirect(url_for('q4'))
    elif 'both' in request.form:
        session['q3'] = 'both'
        return redirect(url_for('q4'))
    elif 'lower' in request.form:
        session['q3'] = 'lower'
        return redirect(url_for('q4'))

    return render_template('classify6s.html', title='Question 3')


@app.route('/Question4', methods=['GET', 'POST'])
def q4():
    # debugging block
    print("---VALUES---")
    for key in session:
        print(key, session[key])
    # end debugging block

    if 'first' in request.form:
        session['q4'] = 'first'
        return redirect(url_for('q5'))
    elif 'second' in request.form:
        session['q4'] = 'second'
        return redirect(url_for('q5'))
    elif 'third' in request.form:
        session['q4'] = 'third'
        return redirect(url_for('q5'))

    return render_template('malloclusion.html', title='Question 4')


@app.route('/Question5', methods=['GET', 'POST'])
def q5():
    # debugging block
    print("---VALUES---")
    for key in session:
        print(key, session[key])
    # end debugging block

    if 'yes' in request.form:
        session['q5'] = 'yes'
        return redirect(url_for('q6'))
    elif 'no' in request.form:
        session['q5'] = 'no'
        return redirect(url_for('q6'))

    return render_template('crowding.html', title='Question 5')


@app.route('/Question6', methods=['GET', 'POST'])
def q6():
    if 'yes' in request.form:
        session['q6'] = 'yes'
        return redirect(url_for('validate'))
    elif 'no' in request.form:
        session['q6'] = 'no'
        return redirect(url_for('validate'))

    return render_template('treatment.html', title='Question 6')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    # extract all the answers from the cookie
    answers = []
    questions = ['Whats the prognosis?', 'Is the 3rd molar present?', 'Whats the classification of the 6th?',
                 'Whats the malloclusion?', 'Is there crowding?', 'Is orthodontic treatment likely at any stage?']
    for key in session:
        answers.append(session[key])

    if 'yes' in request.form:
        return redirect(url_for('outcome'))
    elif 'no' in request.form:
        session.clear()
        return redirect(url_for('index'))

    return render_template('validate.html', title='Is this Correct?', data=answers, questions=questions)


@app.route('/outcome', methods=['GET', 'POST'])
def outcome():
    # extract all the answers from the cookie
    answers = []
    questions = ['Whats the prognosis?', 'Is the 3rd molar present?', 'Whats the classification of the 6th?',
                 'Whats the malloclusion?', 'Is there crowding?', 'Is orthodontic treatment likely at any stage?']
    for key in session:
        answers.append(session[key])

    if 'restart' in request.form:
        session.clear()
        return redirect(url_for('index'))

    return render_template('outcome.html', title='Outcome')

@app.route('/restore', methods=['GET', 'POST'])
def restore():
    return render_template('restore.html', title='Restore')


@app.route('/extract', methods=['GET', 'POST'])
def extract():
    return render_template('extract.html', title='Restore')

@app.route('/moreinfo', methods=['GET', 'POST'])
def moreinfo():
    return render_template('moreinfo.html', title='Restore')

