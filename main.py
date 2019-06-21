from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    username=''
    password=''
    verpassword=''
    email=''
    return render_template('index.html', title='Signup', username=username, password=password, verpassword=verpassword, email=email)


@app.route('/welcome', methods=['POST'])
def welcome():
    username=request.form['username']
    password=request.form['password']
    verpassword=request.form['ver-password']
    email=request.form['email']
    if username=='' or len(username)<3 or len(username) > 20:
        return render_template('index.html', usererror='y', username=username)
    else:
        for char in username:
            if char==' ':
                return render_template('index.html', usererror='y', username=username, email=email)
        return render_template('welcome.html', title='Welcome',username=username)
    if password=='' or len(password)<3 or len(password)>20:
        return render_template('index.html', passerror='y', username=username, email=email)

app.run()