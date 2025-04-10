# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
VALID_ID = "12319585"
VALID_PASSWORD = "12319585"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id == VALID_ID and password == VALID_PASSWORD:
        return redirect(url_for('main'))
    else:
        return "Invalid credentials", 401

@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)