from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html', title='Signup')


@app.route('/welcome', methods=['POST'])
def welcome():
    username=request.form['username']
    return render_template('welcome.html', title='Welcome',username=username )

app.run()