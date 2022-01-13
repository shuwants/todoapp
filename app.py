from flask import Flask
# from flask module, import Flask class.
from flask_sqlalchemy import SQLAlchemy
# from the flask_sqlalchemy library, import SQLAlchemy class.

app = Flask(__name__)
# It's standard way to create flask application.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ShujiKatoMBPro@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ =  'persons' # by default use table name already set, but if we want, we can specify table name with "__tablename__ = ".
    id = db.Column(db.Integer, primary_key=True) # we don't need __init__ because of these lines.
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/') # "@app.route('/')" = decorator, from here, we can tell our Flask application which endpoint to listen to for connections. This time, we want to listen to the homepage route =(root route '/').
def index(): # index is a standard name for the route handler that listens for connections to the root route and figures out what to do next.
    return f'Hello, World!'
