from app import db


class Users(db.Model):
    id=db.column(db.Integer,primary_key=True)
    email=db.column(db.String(120),unique=True,nullable=False)
    full_name=db.column(db.String(120),nullable=False)
    password=db.column(db.String(120),nullable=False)
    qualification=db.column(db.String(120))
    DOB=db.column(db.Date)
    scores=db.relationship('Scores',backref='user',lazy=True)

class Subject(db.Model):
    id=db.column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    description=db.column(db.Text)
    chapters=db.relationship('Chapters',backref='subject',lazy=True)
class Chapters(db.Model):
    id=db.column(db.Integer,primary_key=True)
    name=db.column(db.String(120),nullable=False)
    description=db.column(db.Test)
    subject_id=db.column(db.Integer,db.ForegionKey('subject.id'),nullable=False)
    
    quizzes=db.relationship('Quiz',backref='chapter',lazy=True)
class Quiz(db.Model):
    id=db.column(db.Integer,primary_key=True)
    chapter_id=db.column(db.Integer,db.ForegionKey('chapter.id'),nullable=False)
    date_of_quiz=db.column(db.Date)
    time_duration=db.column(db.Integer,nullable=False)

    questions=db.relationship('Question',backref='quiz',lazy=True)
class Question(db.Model):
    id=db.column(db.Integer,primary_key=True)
    question_statement=db.column(db.Text,nullable=False)
    option1=db.column(db.String(120),nullable=False)
    option2=db.column(db.String(120),nullable=False)
    option3=db.column(db.String(120),nullable=False)
    option4=db.column(db.String(120),nullable=False)
    correct_option=db.column(db.String(120),nullable=False)
    quiz_id=db.column(db.Integer,db.ForegionKey('quiz.id'),nullable=False)

class Scores(db.Model):
    id=db.column(db.Integer,primary_key=True)
    total_score=db.column(db.Integer,nullable=False)
    timestamp=db.column(db.DateTime,default=db.func.current_timestamp())
    quiz_id=db.column(db.Integer,db.ForegionKey('quiz.id'),nullable=False)
    user_id=db.column(db.Integer,db.ForegionKey('users.id'),nullable=False)