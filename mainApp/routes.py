from flask import Flask, render_template, url_for, redirect, flash
from mainApp import app, db
from mainApp.forms import AddQuestionType1Form, AddQuestionType2Form
from mainApp.models import QuestionTypeOne, QuestionType2

@app.route("/")
@app.route("/home")
def home():
    type1questions=QuestionTypeOne.query.all()
    return render_template('home.html', title='Home', type1questions=type1questions)

@app.route("/add_question_type1", methods=['POST', 'GET'])
def add_question_type1():
    form = AddQuestionType1Form()
    if form.validate_on_submit():
        question = QuestionTypeOne(question=form.question.data, answer_options=form.answer_options.data, correct_answer=form.correct_answer.data, marks_available=form.marks_available.data, question_tags=form.question_tags.data, answer_feedback=form.answer_feedback.data)
        db.session.add(question)
        db.session.commit()
        flash('Question added.')
        return redirect(url_for('home'))
    return render_template('add_question_type1.html',title='Add Multiple Choice Question', form=form)

@app.route("/addtextquestion", methods=['GET','POST'])
def addtextquestion():
    form = AddQuestionType2Form()
    if form.validate_on_submit():
        question2 = QuestionType2(name = form.name.data, shortDescription = form.shortDescription.data, question = form.question.data, answer = form.answer.data, instantFeedback = form.instantFeedback.data, marksAwarded = form.marksAwarded.data)
        db.session.add(question2)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addq2.html', title = 'Add Text Question', form=form)