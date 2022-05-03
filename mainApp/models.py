from mainApp import db
from datetime import date,datetime,timedelta

class QuestionTypeOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer_option_1 = db.Column(db.Text, nullable=False)
    answer_option_2 = db.Column(db.Text, nullable=False)
    answer_option_3 = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    marks_available = db.Column(db.Integer, nullable=False)
    correct_answer_feedback = db.Column(db.Text, nullable=False)
    incorrect_answer_feedback = db.Column(db.Text, nullable=False)
    feedforward_comments = db.Column(db.Text, nullable=False)
    question_tag_1 = db.Column(db.Text, nullable=False)
    question_tag_2 = db.Column(db.Text, nullable=False)
    question_tag_3 = db.Column(db.Text, nullable=False)
    assessmentID = db.Column(db.Integer,db.ForeignKey('asessment.id'), nullable=False)



class QuestionType2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionType = db.Column(db.Integer, nullable= False)
    name = db.Column(db.Text, nullable=False)
    shortDescription = db.Column(db.Text, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    correctFeedback = db.Column(db.Text, nullable=False)
    incorrectFeedback = db.Column(db.Text, nullable=False)
    marksAwarded = db.Column(db.Integer, nullable=False)
    assessmentID = db.Column(db.Integer,db.ForeignKey('asessment.id'), nullable=False)

    def __repr__(self):
        return f"QuestionType2('{self.name}', '{self.shortDescription}', '{self.question}', '{self.answer}' , '{self.correctFeedback}','{self.incorrectFeedback}','{self.marksAwarded}')"



class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer, nullable= False)
    studentID = db.Column(db.Integer, nullable= False)

# Assessment
class Asessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_title = db.Column(db.Integer,nullable=False)
    assessment_difficulty = db.Column(db.Integer,nullable=False) 
    assessment_type = db.Column(db.Integer,nullable=False)
    date_created_on = db.Column(db.DateTime,default=datetime.now)
    questiontypeone = db.relationship('QuestionTypeOne', backref='Assessment', lazy=True, cascade='all, delete-orphan')
    questiontypetwo = db.relationship('QuestionType2', backref='Assessment', lazy=True, cascade='all, delete-orphan')