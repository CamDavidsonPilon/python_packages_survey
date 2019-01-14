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
    id = db.Column(db.Integer(), primary_key=True)
    test = db.Column(db.Boolean(), nullable=True)
    platform = db.Column(db.String(256), nullable=True)
    packages = db.Column(db.Array(db.String(256)), nullable=True)

    def __init__(self, test, platform):
        self.test = test
        self.platform = platform
        self.packages = packages


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()

    row = Environment(data['test'], data['platform'][:256], data['packages'])
    
    db.session.add(row)
    db.session.commit()
    
    return "a-okay", 200