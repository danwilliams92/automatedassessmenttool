from mainApp import db
"""
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_one_questions = db.relationship('QuestionTypeOne', backref='assessment', passive_deletes=True)
"""

class QuestionTypeOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    
    #need to use JSON data type here to place a list into the column
    answer_options = db.Column(db.Text, nullable=False)

    correct_answer = db.Column(db.String, nullable=False)
    marks_available = db.Column(db.Integer, nullable=False)
    answer_feedback = db.Column(db.Text, nullable=False)
    question_tags = db.Column(db.Text, nullable=False)
    #assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id', ondelete="CASCADE"), nullable=False)