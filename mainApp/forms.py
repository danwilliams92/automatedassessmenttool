from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError

class AddQuestionType1Form(FlaskForm):
  question = StringField('Question',validators=[DataRequired()])
  answer_options = StringField('Answer options (please give three options, separated by a comma)',validators=[DataRequired()])
  correct_answer = StringField('Correct answer',validators=[DataRequired()])
  marks_available = IntegerField('Marks available for question', validators=[DataRequired()])
  question_tags = StringField('Relevant question tags (please give three category tags, separated by a comma)', validators=[DataRequired()])
  correct_answer_feedback = TextAreaField('Feedback to provide with correct answer', validators=[DataRequired()])
  incorrect_answer_feedback = TextAreaField('Feedback to provide with incorrect answer', validators=[DataRequired()])
  feedforward_comments = TextAreaField('Feedforward comments for student to continue/strengthen learning', validators=[DataRequired()])
  add_question = SubmitField('Add question to assessment')

class AddQuestionType2Form(FlaskForm):
  name = StringField('Question Name', validators=[DataRequired()])
  shortDescription = TextAreaField('Add a brief description')
  question = TextAreaField('Please input the question', validators=[DataRequired()])
  answer = TextAreaField('Please input the answer', validators=[DataRequired()])
  correctFeedback = TextAreaField('Please input instant feedback for a correct answer', validators=[DataRequired()])
  incorrectFeedback = TextAreaField('Please input instant feedback for an incorrect answer', validators=[DataRequired()])
  marksAwarded = IntegerField('Please input the points awarded for a correct answer', validators=[DataRequired()])
  submit = SubmitField('Submit question')

class selectQuestionTypeForm(FlaskForm):
  type = SelectField('Select the type of question you wish to add', choices=['Multiple Choice','Question and response'])
