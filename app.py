from flask import Flask,render_template,request,redirect
# session[logged_in]
import api
from db import Database


app = Flask(__name__)

dbo = Database()


@app.route('/')

def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response  = dbo.insert(name, email, password)


    if response:
        return render_template('login.html',message="Registration successful.Kindly login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.search(email,password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message="Incorrect email/password")

@app.route('/profile')

def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('NER.html')

@app.route('/perform_ner',methods=['post'])
@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)  # Debugging: Check the API response structure

    result = ''
    if 'entities' in response:
        for i in response['entities']:
            # Access the keys that exist in the response
            entity_text = i.get('text', 'Unknown')
            entity_type = i.get('type', 'Unknown')
            result += f"{entity_text} ({entity_type})\n"
    else:
        result = "No entities found in the text."

    return render_template("NER.html", result=result)


app.run(debug=True)
