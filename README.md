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

To create the tables for the first time:
```

$ FLASK_APP=main.py DBUSER="" DBPASS="" DBHOST="" DBNAME="testdb"  python 
> from main import db
> db.create_all()  # inverse is db.drop_all()

```




Run the flask server

```
$ FLASK_APP=main.py DBUSER="" DBPASS="" DBHOST="" DBNAME="testdb"  python -m flask run
```

#### Deploy

To deploy (Python 2.7 required)

```
gcloud app deploy
```
https://pip-project-survey.appspot.com/

