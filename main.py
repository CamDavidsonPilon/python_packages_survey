from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    print(data)
    return "a-okay", 200