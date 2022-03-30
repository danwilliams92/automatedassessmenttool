from mainApp import db

class QuestionTypeOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    
    #need to use JSON data type here to place a list into the column
    answer_options = db.Column(db.Text, nullable=False)

    correct_answer = db.Column(db.String, nullable=False)
    marks_available = db.Column(db.Integer, nullable=False)
    answer_feedback = db.Column(db.Text, nullable=False)
    question_tags = db.Column(db.Text, nullable=False)

class QuestionType2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shortDescription = db.Column(db.Text, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    correctFeedback = db.Column(db.Text, nullable=False)
    incorrectFeedback = db.Column(db.Text, nullable=False)
    marksAwarded = db.Column(db.Integer, nullable=False)
    #TAKEN OUT UNTIL WE HAVE ASSESSMENT  assessmentID = db.relationship('Assessment', backref ='questiontype2', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"QuestionType2('{self.name}', '{self.shortDescription}', '{self.question}', '{self.answer}' , '{self.correctFeedback}','{self.incorrectFeedback}','{self.marksAwarded}')"