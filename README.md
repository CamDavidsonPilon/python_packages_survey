# Python Packages Survey

** WIP expect production data to be deleted **

https://www.notion.so/Why-are-we-doing-this-332c3898242a4ce8bf7b784b9e1afa62

## Development 

#### Local Development 

The main app is Python 3.6+:

```
$ brew install python3
$ pip3 install -r requirements.txt
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

Run the flask server locally

```
$ FLASK_ENV=development FLASK_APP=main.py  python -m flask run
```

visit localhost:5000

#### Deployment and Production

To deploy (Python 2.7 required)

```
gcloud app deploy
```


To modify the tables in prod GCP (run `./cloud_sql_proxy`)
```

$ DBUSER=postgres DBPASS=<pass> INSTANCE_CONNECTION_NAME=pip-project-survey:northamerica-northeast1:testdb DBDATABASE=testdb ipython
> from main import db
> db.create_all()  # inverse is db.drop_all()

```

