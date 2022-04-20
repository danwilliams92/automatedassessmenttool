from flask import Flask, render_template, url_for, redirect, flash
from mainApp import app, db
from mainApp.forms import AddQuestionType1Form, AddQuestionType2Form, selectQuestionTypeForm
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

@app.route("/add_text_question", methods=['GET','POST'])
def addtextquestion():
    form = AddQuestionType2Form()
    if form.validate_on_submit():
        question2 = QuestionType2(questionType = 2, name = form.name.data, shortDescription = form.shortDescription.data, question = form.question.data, answer = form.answer.data, correctFeedback = form.correctFeedback.data, incorrectFeedback = form.incorrectFeedback.data, marksAwarded = form.marksAwarded.data)
        db.session.add(question2)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('addq2.html', title = 'Add Text Question', form=form)

@app.route("/addaquestion", methods=['GET','POST'])
def addaquestion():
    form = selectQuestionTypeForm()
    return render_template('questiontype.html', form=form)

@app.route('/temp_question_2_list')
def question2List():
    type2Questions = QuestionType2.query.all()
    return render_template('temp_question_list.html',type2Questions=type2Questions) 

@app.route('/question_type_2/<int:question_id>')
def questionType2(question_id):
    type2Questions = QuestionType2.query.get_or_404(question_id)
    return render_template('question_type_2.html', type2Questions=type2Questions)

@app.route('/question_type_2/edit/<int:question_id>', methods=['GET','POST'])
def edit_question_2(question_id):
    type2Questions = QuestionType2.query.get_or_404(question_id)
    form = AddQuestionType2Form()
    if form.validate_on_submit():
        type2Questions.name = form.name.data
        type2Questions.shortDescription = form.shortDescription.data
        type2Questions.question = form.question.data
        type2Questions.answer = form.answer.data
        type2Questions.correctFeedback = form.correctFeedback.data
        type2Questions.incorrectFeedback = form.incorrectFeedback.data
        type2Questions.marksAwarded = form.marksAwarded.data
        db.session.add(type2Questions)
        db.session.commit()
        flash('Successfully updated post')
        return redirect(url_for('question2List'))
    form.name.data = type2Questions.name
    form.shortDescription.data = type2Questions.shortDescription
    form.question.data = type2Questions.question
    form.answer.data = type2Questions.answer
    form.correctFeedback.data = type2Questions.correctFeedback
    form.incorrectFeedback.data = type2Questions.incorrectFeedback
    form.marksAwarded.data = type2Questions.marksAwarded
    return render_template('edit_questions_2.html', form=form, type2Questions=type2Questions)


@app.route('/question_type_2/delete/<int:question_id>')
def delete_question_type_2(question_id):
    question_to_delete = QuestionType2.query.get_or_404(question_id)
    db.session.delete(question_to_delete)
    db.session.commit()
    flash('Successfully deleted question.')
    return redirect(url_for('question2List'))
