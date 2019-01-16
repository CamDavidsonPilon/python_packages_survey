import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import sqlalchemy

import utils


if utils.is_gcp():
    # https://cloud.google.com/appengine/docs/flexible/python/using-cloud-sql-postgres
    database_uri = 'postgresql+psycopg2://{USER}:{PASSWORD}@/{DATABASE}?host=/cloudsql/{INSTANCE_CONNECTION_NAME}'.format(
        USER=os.environ['DBUSER'],
        PASSWORD=os.environ['DBPASS'],
        DATABASE=os.environ['DBDATABASE'],
        INSTANCE_CONNECTION_NAME=os.environ['INSTANCE_CONNECTION_NAME']
    )
else:
    database_uri = 'postgresql+psycopg2://:@/testdb'


app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)



class Environment(db.Model):
    id =             db.Column(db.Integer(), primary_key=True)
    test =           db.Column(db.Boolean())
    platform =       db.Column(db.String(256))
    uuid =           db.Column(db.String(256))
    packages =       db.Column(db.ARRAY(db.String(256)))
    primary_use =    db.Column(db.Enum('science & engineering', 'web development', 'education', 'scripting', 'software development', 'other', name='primary_use'))
    python_version = db.Column(db.String(64))
    years_using_python = db.Column(db.Integer())

    def __init__(self, test, platform, uuid, packages, primary_use, python_version, years_using_python):
        self.test = test
        self.platform = platform
        self.packages = packages
        self.uuid = uuid
        self.primary_use = primary_use
        self.python_version = python_version
        self.years_using_python = years_using_python




@app.route('/')
def home():
    email = "cam.davidson.pilon@gmail.com"
    count = 3
    return render_template('index.html', count=count, email=email)


@app.route('/collect', methods=['POST', 'GET'])
def collect():

    if request.method == 'POST':
        data = request.get_json()
        libs = utils.load_from_disk_pypi_libraries()
        public_libs = [(name, version) for (name, version) in data['list_of_installed_packages'] if name in libs]

        row = Environment(
            data['test'], 
            data['platform'], 
            data['uuid'],
            public_libs,
            data['primary_use'],
            data['python_version'],
            data['years_using_python'],
        )
        try:
            db.session.add(row)
            db.session.commit()
        except sqlalchemy.exc.DataError:
            return "Data validation error", 400

        return "a-okay", 200