from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    username=''
    email=''
    return render_template('index.html', title='Signup', username=username, email=email)


@app.route('/welcome', methods=['POST'])
def welcome():
    username=request.form['username']
    password=request.form['password']
    verpassword=request.form['ver-password']
    email=request.form['email']
    user_error=''
    pass_error=''
    verpass_error=''
    email_error=''
    verpass_valid=''
    def is_valid(word):
        if word=='' or len(word) < 3 or len(word) > 20:
            return False
        else:
            for char in word:
                if char==' ':
                    return False
            return True
    def are_matching(password,verpassword):
        if verpassword == '':
            return False
        if password == verpassword:
            return True
        else:
            return False

    def is_valid_email(email):
        if email == '':
            return True
        if len(email) < 3 or len(email) > 20:
            return False
        at = 0
        periods = 0
        for char in email:
            if char == '@':
                at += 1
            if char == '.':
                periods += 1
        if at ==1 and periods ==1:
            return True
        else:
            return False
        
    
    if not is_valid(username):
        user_error = 'y'
    
    if not is_valid(password):
        pass_error = 'y'
    
    if not are_matching(password,verpassword):
        verpass_error = 'y'

    if not is_valid(verpassword):
        verpass_valid = 'y'
        verpass_error = ''
    
    if not is_valid_email(email):
        email_error = 'y'
    
    if not is_valid(username) or not is_valid(password) or not is_valid(verpassword) or not are_matching(password, verpassword) or not is_valid_email(email):
        return render_template('index.html', verpassvalid = verpass_valid, emailerror=email_error, verpassworderror=verpass_error, passerror=pass_error,  usererror=user_error, username=username, email=email)
    
    else:
        return render_template('welcome.html', title='Welcome', username=username)

app.run()
