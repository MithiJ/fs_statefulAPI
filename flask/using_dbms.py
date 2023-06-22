from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mithijethwa@localhost:5432/mydatabase"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(50))
    stats = db.Column(db.Integer)

@app.route('/set')
def set():
    filepath = request.args.get('filepath')
    # URL: http://127.0.0.1:5000/set?filepath=xyz
    file = User(filepath=str(filepath), stats=10)
    db.session.add(file)
    db.session.commit()
    return 'ok'

# Now instead of getting the db, we are getting a column of the db or performing
# data analysis on the db as is.
@app.route('/getcolumn')
def get():
    col_id = request.args.get('id')
    '''
    When getting we can use user authentication and see if they have the 
    necessary access for the dataframe they are trying to access.
    '''
    file = User.query.get(col_id)
    if file:
        return f"User ID: {file.id}, Name: {file.filepath}"
    else:
        return 'User not found'
