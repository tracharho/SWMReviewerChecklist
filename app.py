from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
import smtplib, os, get_data_from_csvs, io
from makeletter import makeLetter
from docx import Document
from docx.shared import Inches, Pt

app = Flask(__name__, static_folder='static') #turn this file into a web application
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

###ADD SECRET KEY###
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

get_data_from_csvs.categorizeCsvs()

@app.route("/") #listen to get r`equests on slash
def index():
    return render_template("index.html") 

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

"""Remember to go to terminal and do
$ export FLASK_APP=application
$ flask run
to start the webserver"""
#DEbug mode export FLASK_ENV=development

#Use serverside to check for logic and prevent malicious use. 
#Javascript can be disabled from the frontend