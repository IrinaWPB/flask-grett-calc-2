from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def says_welcome():
    return 'Welcome'

@app.route('/welcome/home')
def says_welcome_home():
    return 'Welcome home'

@app.route('/welcome/back')
def says_welcome_back():
    return 'Welcome back'

