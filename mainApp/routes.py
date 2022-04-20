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

@app.route("/delete_type_one_question/<id>")
def delete_type_one_question(id):
    type_one_question = QuestionTypeOne.query.filter_by(id=id).first()
    if not type_one_question:
        flash("Question does not exist", category="error")
    else:
        db.session.delete(type_one_question)
        db.session.commit()
        flash("Question deleted", category="success")
    return redirect(url_for('home'))

#update so that this actually changes the database row
@app.route("/edit_type_one_question/<id>", methods=['POST', 'GET'])
def edit_type_one_question(id):
    type_one_question = QuestionTypeOne.query.filter_by(id=id).first()
    form = AddQuestionType1Form()
    if form.validate_on_submit():
        type_one_question.question = form.question.data
        type_one_question.answer_options = form.answer_options.data
        type_one_question.correct_answer = form.correct_answer.data
        type_one_question.marks_available = form.marks_available.data
        type_one_question.question_tags = form.question_tags.data
        db.session.add(type_one_question)
        db.session.commit()
        flash('Question updated.')
        return redirect(url_for('home'))
    form.question.data = type_one_question.question 
    form.answer_options.data = type_one_question.answer_options 
    form.correct_answer.data = type_one_question.correct_answer
    form.marks_available.data = type_one_question.marks_available
    form.question_tags.data = type_one_question.question_tags
    form.answer_feedback.data = type_one_question.answer_feedback
    
    return render_template('edit_type_one_question.html',title='Edit Multiple Choice Question', form=form, type_one_question=type_one_question)