from flask import Flask, render_template, url_for
from main import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')
