from flask import Flask, render_template, request, redirect, send_file, flash, url_for
from app import app
from app.forms import LoginForm
from app.makeletter import makeLetter
from flask_sqlalchemy import SQLAlchemy


@app.route("/") #listen to get r`equests on slash
@app.route("/index")
def index():
    return render_template('index.html') 

@app.route("/") #listen to get r`equests on slash
def test():
    return render_template("test.html")

@app.route("/register", methods=["POST"])
def register():
    if request.method == 'POST':        
        comments = request.form.getlist('checkbox')
        reviewername = request.form.get('reviewer-name')
        recipientname = request.form.get('recipient')
        projectname = request.form.get('projectname')
        dscnumber = request.form.get('dscnumber')
        letter_path, letter_name = makeLetter(reviewername, recipientname, projectname, dscnumber, comments)
        try:
            return send_file(letter_path, as_attachment=True, attachment_filename=letter_name)
        except Exception as e:
            print ("IDK WHAT HAPPENED BOSS")