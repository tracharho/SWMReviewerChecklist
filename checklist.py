from app import app, db
from app.models import User, Project, ModifiedRow, OriginalRow
from app.csvdata import createChecklistJSON

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Project':Project, 'ModifiedRow':ModifiedRow, 'OriginalRow':OriginalRow}


#to do model editings in shell
# The original rows table needs to be precreated via the createChecklistJSON function after a db deletion
# MAKE SURE YOU'RE IN THE RIGHE DIRECTORY
# Comment out ui.run in __init__.py
# $ export FLASK_APP=checklist.py
# $ flask shell
# >>> from app import db
# >>> db.create_all() #initializes the database.
# >>> from app.csvdata import createChecklistJSON as cCJ
# >>> cCJ()
# >>> db.session.commit()
# Note that sometiems the database needs to be deleted to be re iniitailized. 
# THe corresponding flask db migration folder needs to be deleted as well
# $ flask db init
# $ flask db migrate -m "Initial Migration"
# # flask db upgrade

