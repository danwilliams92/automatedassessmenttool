from flask import Flask, render_template, url_for, redirect, flash
from mainApp import app, db
from mainApp.forms import AddQuestionType1Form
from mainApp.models import QuestionTypeOne

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
