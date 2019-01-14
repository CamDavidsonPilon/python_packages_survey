import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False, # I think I can remove
)

db = SQLAlchemy(app)


class Environment(db.Model):
    id =             db.Column(db.Integer(), primary_key=True)
    test =           db.Column(db.Boolean())
    platform =       db.Column(db.String(256))
    uuid =           db.Column(db.String(256))
    packages =       db.Column(db.ARRAY(db.String(256)))
    primary_use =    db.Column(db.String(256))
    python_version = db.Column(db.String(64))

    def __init__(self, test, platform, uuid, packages, primary_use, python_version):
        self.test = test
        self.platform = platform
        self.packages = packages
        self.uuid = uuid
        self.primary_use = primary_use
        self.python_version = python_version


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()

    row = Environment(
        data['test'], 
        data['platform'], 
        data['uuid'],
        data['list_of_installed_packages'],
        data['primary_use'],
        data['python_version'],
    )
    
    db.session.add(row)
    db.session.commit()
    
    return "a-okay", 200