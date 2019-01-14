## PIP Packages Survey


#### Local Development 

The main app is Python 3.7:

```
$ pip install -r requirements.txt
```

```
$ brew install postgres
$ brew services start postgresql
```

To create the database for the first time: `createdb testdb`.

To create the tables locally for the first time:
```

$ python 
> from main import db
> db.create_all()  # inverse is db.drop_all()

```


To modify the tables in prod GCP:
```

$ DBUSER=postgres DBPASS=<pass> INSTANCE_CONNECTION_NAME=pip-project-survey:northamerica-northeast1:testdb DBDATABASE=testdb ipython
> from main import db
> db.create_all()  # inverse is db.drop_all()

```


Run the flask server locally

```
$ FLASK_APP=main.py  python -m flask run
```

#### Deploy

To deploy (Python 2.7 required)

```
gcloud app deploy
```
https://pip-project-survey.appspot.com/
https://pip-packages-survey.com/

