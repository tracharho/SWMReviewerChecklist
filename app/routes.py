from flask import Flask, render_template, session, request, redirect, send_file, flash, url_for, session
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewProjectForm, ChecklistForm
from app.models import User, Project, Checklist, ModifiedRow, OriginalRow
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.makeletter import makeLetter
from flask_sqlalchemy import SQLAlchemy
from app.csvdata import createChecklistJSON


@app.route("/") 
@app.route("/landing")
def landing():
    return render_template('landing.html')

 
 #listen to get requests on slash
@app.route("/index")
@login_required
def index():
    if current_user.is_authenticated:
        return render_template('index.html', title='HOME PAGE TITLE') 
    return render_template('index.html', title='HOME PAGE TITLE') 

@app.route("/<username>/projectlist", methods=['GET','POST'])
@login_required
def projectlist(username): 
    return render_template('projects.html', username=username, projects=current_user.projects, title='PROJECT LIST') 


#HIDDEN CSRF TOKEN???
# cl : local checklist variable name
#TODO CLEAN UP JIINJA AND LOCAL VARIABLE NAMES
@app.route("/<username>/<projectname>/checklist/", methods=["GET", "POST"])
@login_required
def checklist(username,projectname):
    current_project = Project.query.filter_by(name=projectname).first()
    if current_project.checklist_is_original == True:
        list_of_rows = OriginalRow.query.all()
    form = ChecklistForm()
    #Functions.js first sets all checkbox values to be equal to the entry box
    #Then the POST method gets all checked values.
    if request.method == 'POST':        
        #changed html submit tag to have name 'but' and value 'Submit'
        if request.form['but'] == 'Submit':
            comments = request.form.getlist('checkbox')
            reviewername = current_user.username
            recipientname = current_project.recipient
            projectname = current_project.name
            dscnumber = current_project.dsc_number
            letter_path, letter_name = makeLetter(reviewername, recipientname, projectname, dscnumber, comments)
            try:
                return send_file(letter_path, as_attachment=True, attachment_filename=letter_name)
            except Exception as e:
                print ("IDK WHAT HAPPENED BOSS")
        if request.form['but'] == 'Save':
            reference = request.form.getlist('comment')
            print('reference', reference)
            print('---')
        else:
            return('ERROR')
    # checklist.html calls the generate.js script to populate all of the 
    # rows based on the json generated from csvdata.categorizeCSVs()
    return render_template('checklist.html', title='CHECKLIST', current_project=current_project, username=username, form=form, list_of_rows=list_of_rows)


@app.route('/login', methods=['GET', 'POST'])
def login():
    #in the case that the user is already logged in but finds the login page again.
    if current_user.is_authenticated:
        return redirect(url_for('landing'))
    form = LoginForm()
    #if all the required fields are filled out, execute this block of code
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            #flash shows a message to the user
            flash('Username or Password not recognized.'.format(form.username.data, form.remember_me.data))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '': 
            next_page = url_for('projectlist', username=user.username)
        return redirect(next_page)   
    return render_template('login.html',title='Sign In', form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out!')
    return redirect(url_for('landing'))

@app.route('/new_project', methods=['GET','POST'])
@login_required
def new_project():
    form = NewProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.project_name.data, dsc_number=form.dsc_number.data, recipient=form.recipient.data ,author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Project has been saved!')
        return redirect(url_for('projectlist', username=current_user.username))
    return render_template('newproject.html', title='New Project', form=form)
    