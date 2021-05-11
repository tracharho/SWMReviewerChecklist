from app import app, db
from app.models import User, Project, ModifiedRow, OriginalRow
from app.csvdata import createChecklistJSON

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Project':Project, 'ModifiedRow':ModifiedRow, 'OriginalRow':OriginalRow}


#to do model editings in shell
# MAKE SURE YOU'RE IN THE RIGHE DIRECTORY
# $ export FLASK_APP=checklist.py
# >>> createChecklistJSON()
# >>> db.create_all() #initializes the database.
# Note that sometiems the database needs to be deleted to be re iniitailized. 
# The original rows table needs to be recreated via the createChecklistJSON function after a db deletion

