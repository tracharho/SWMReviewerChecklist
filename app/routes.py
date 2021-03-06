from flask import Flask, render_template, session, request, redirect, send_file, flash, url_for, session
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewProjectForm, ChecklistForm, ProjectListForm
from app.models import User, Project, ModifiedRow, OriginalRow
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.makeletter import makeLetter
from flask_sqlalchemy import SQLAlchemy
from app.csvdata import createChecklistJSON
from sqlalchemy.orm.session import make_transient
import os

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
    form = ProjectListForm() 
    if request.method == 'POST':
        if request.form['but'] == 'Delete':
            selected_projects = request.form.getlist('checkbox')
            for project in selected_projects:
                db.session.delete(Project.query.filter_by(name=project).first())  
            #print(ModifiedRow.query.filter_by(parent_project_id==None))
            #db.session.delete(ModifiedRow.query.filter_by(parent_project_id=False).all())          
            db.session.commit()
    return render_template('projects.html', username=username, projects=current_user.projects, title='PROJECT LIST', form=form) 


#HIDDEN CSRF TOKEN???
# cl : local checklist variable name
@app.route("/<username>/<projectname>/checklist/", methods=["GET", "POST"])
@login_required
def checklist(username,projectname):
    current_project = Project.query.filter_by(name=projectname).first()
    list_of_rows = OriginalRow.query.all()
    list_of_saved_row_numbers = []
    list_of_saved_row_comments = []
    if current_project.checklist_is_original == True:
        pass
    else:
        #TODO Addin logic to insert the edited rows.
        list_of_saved_rows = ModifiedRow.query.filter_by(parent_project_id=current_project.id).all()
        for n in list_of_saved_rows:
            list_of_saved_row_numbers.append(n.row_number)
            list_of_saved_row_comments.append(n.Comment)
        # i
        for original_row in list_of_rows:
            if original_row.row_number in list_of_saved_row_numbers:
                db.session.expunge(original_row)
                make_transient(original_row)
                index = list_of_saved_row_numbers.index(original_row.row_number)
                original_row.Comment = list_of_saved_row_comments[index]
                original_row.checked = True
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
            projectnumber = current_project.dsc_number
            letter_path, letter_name = makeLetter(reviewername, recipientname, projectname, projectnumber, comments)
            return send_file(letter_path, as_attachment=True, attachment_filename=letter_name)
        # Check if modified exist. If it does, then don't save. 
        # Ensure overwriting is correct
        # PLEASE REFACTOR ME, MY VARIABLE NAMES ARE NOT CLEAR
        if request.form['but'] == 'Save':
            saved_comments = request.form.getlist('checkbox')   #returns the value of all checkbox items from DOM
            current_project.checklist_is_original = False   
            newly_saved_rows = []
            for rows in saved_comments:
                saved_row_number, saved_comment = rows.split('|')[0], rows.split('|')[1]
                newly_saved_rows.append(saved_row_number)
                existing_saved_row = ModifiedRow.query.filter_by(parent_project_id=current_project.id, row_number=saved_row_number).first()
                if existing_saved_row is None:
                    saved_row = ModifiedRow(row_number=saved_row_number, Comment=saved_comment, parent_project_id=current_project.id)
                else:
                    db.session.delete(existing_saved_row)
                    saved_row = ModifiedRow(row_number=saved_row_number, Comment=saved_comment, parent_project_id=current_project.id)
                db.session.add(saved_row)
            print(saved_comments)#if there are saved comments from a previous session
            for saved_row_number in list_of_saved_row_numbers: # if there are new saved
                unchecked_row = ModifiedRow.query.filter_by(parent_project_id=current_project.id, row_number=saved_row_number).first()
                if unchecked_row.row_number not in newly_saved_rows:
                    print(unchecked_row.row_number)
                    db.session.delete(unchecked_row)
            db.session.commit()
            print('commited')
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '': 
                next_page = url_for('projectlist', username=current_user.username)
            return redirect(next_page)   
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
        flash('You have registered.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You logged out.')
    return redirect(url_for('landing'))

@app.route('/new_project', methods=['GET','POST'])
@login_required
def new_project():
    form = NewProjectForm()
    if form.validate_on_submit():
        project = Project(name = form.project_name.data, dsc_number = form.project_number.data, 
            recipient = form.recipient.data, disturbed_area = form.disturbed_area.data,
            rpa_present=form.rpa_present.data, rma_present=form.rma_present.data, 
            wmp_present=form.wmp_present.data, bmp_recording_reqd=form.bmp_recording_reqd.data, 
            wetlands_present=form.wetlands_present.data, author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Project has been saved!')
        return redirect(url_for('projectlist', username=current_user.username))
    return render_template('newproject.html', title='New Project', form=form)
    
