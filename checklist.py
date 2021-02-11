from app import app, db
from app.models import User, Project, Checklist, ModifiedRow, OriginalRow

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Project':Project, 'Checklist':Checklist, 'ModifiedRow':ModifiedRow, 'OriginalRow':OriginalRow}

#to do model editings in shell
# $ export FLASK_APP=checklist.py

# MAKE SURE YOU'RE IN THE RIGHE DIRECTORY