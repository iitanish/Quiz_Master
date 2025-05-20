from app import create_app
from flask import render_template
from app.models import Users,Subject,Chapters,Quiz,Question,Scores
app=create_app()
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/about')
def about():
    return render_template("about.html")