## PIP Packages Survey


#### Local Development 

The main app is Python 3.7:

```
pip install -r requirements.txt
```

```
brew install postgres
brew services start postgresql
```

To create the database for the first time: `createdb testdb`.



```
$ FLASK_APP=main.py DBUSER="" DBPASS="" DBHOST="" DBNAME="testdb"  python -m flask run
$ python script.py

```

To deploy (Python 2.7 required)

```
gcloud app deploy
```
https://pip-project-survey.appspot.com/

