from flask import Flask, render_template, request, redirect, send_file
import smtplib, os, get_data_from_csvs
from cStringIO import StringIO
from datetime import datetime
from makeletter import makeLetter



app = Flask(__name__, static_folder='static') #turn this file into a web application
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

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
        document = makeLetter(reviewername, recipientname, projectname, dscnumber, comments)
        f = StringIO()
        document.save(f)
        length = f.tell()
        f.seek(0)
        return send_file(f, as_attachment=True, attachment_filename='report.doc')


"""Remember to go to terminal and do
$ export FLASK_APP=application
$ flask run
to start the webserver"""

#Use serverside to check for logic and prevent malicious use. 
#Javascript can be disabled from the frontend