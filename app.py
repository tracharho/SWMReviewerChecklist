#TODO 
#Add collapsible sections 

from flask import Flask, render_template, request, redirect, send_file
import smtplib, os, csv_to_json
from docx import Document
from cStringIO import StringIO
from docx.shared import Inches, Pt
from datetime import datetime

app = Flask(__name__, static_folder='static') #turn this file into a web application

csv_to_json.make_json((os.getcwd()+'/static/Names.csv'), (os.getcwd()+'/static/GOOBAH.json'))

@app.route("/") #listen to get r`equests on slash
def index():
    
    return render_template("index.html") 

@app.route("/register", methods=["POST"])
def register():
    if request.method == 'POST':        
        comments = request.form.getlist('cb')
        document = Make_Letter(comments)
        f = StringIO()
        document.save(f)
        length = f.tell()
        f.seek(0)
        return send_file(f, as_attachment=True, attachment_filename='report.doc')

def Make_Letter(comments):
    doc = Document()
    sections = doc.sections
    sections[0].left_margin,sections[0].right_margin,sections[0].top_margin,sections[0].bottom_margin = Inches(0.75), Inches(0.75), Inches(0.5), Inches(0.5)    # Adding the City Logo
    doc.add_picture(os.getcwd()+'/static/LetterHead.PNG')
    Para1 = doc.add_paragraph('INTER-OFFICE MEMORANDUM')
    Para1.runs[0].style = 'Title Char'
    Para1.add_run('\n\nDATE:').bold=True
    Para1.add_run('\t\t{}'.format(datetime.today().strftime('%m/%d/%Y')))
    Para1.add_run('\nTO:').bold=True
    Para1.add_run('\t\tPTL GOES HERE')
    Para1.add_run('\nFROM:').bold = True
    Para1.add_run('\tCURRENT REVIEWER GOES HERE')
    Para1.add_run('\nSUBJECT:').bold = True
    Para1.add_run('\tPROJECT NUMBER GOES HERE')
    Para1.add_run('\n\t\tDSC Engineering Review Comments')
    Para1.add_run('\n\t\tDSC File: DSC FILE NUMBER GOES HERE').add_break()

    Para2 = doc.add_paragraph('DSC cannot approve the project at this time. The following comments must first be addressed:\n')
    i = 1
    for comment in comments:
        Para2.add_run('\n{}:  {}'.format(i,comment))
        i += 1
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)
    for para in doc.paragraphs:
        para.style = doc.styles['Normal']
    return doc

"""Remember to go to terminal and do
$ export FLASK_APP=application
$ flask run
to start the webserver"""

#Use serverside to check for logic and prevent malicious use. 
#Javascript can be disabled from the frontend