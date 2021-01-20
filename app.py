from flask import Flask, render_template, request, redirect
import smtplib
from docx import Document
from cStringIO import StringIO

app = Flask(__name__) #turn this file into a web application

@app.route("/") #listen to get requests on slash
def index():
    #name = request.args.get("name", "Brian") #read documentation
    return render_template("index.html") 


# @app.route("/register", methods=["POST"])
# def register():
#     name = request.form.get("name")
#     dorm = request.form.get("dorm")
#     if not name or not dorm:
#         return "failure" #returns failure if 
#     return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        comments = request.form.getlist("cb")
        print(comments)
    return render_template("success.html")

"""Remember to go to terminal and do
$ export FLASK_APP=application
$ flask run
to start the webserver"""

#Use serverside to check for logic and prevent malicious use. 
#Javascript can be disabled from the 