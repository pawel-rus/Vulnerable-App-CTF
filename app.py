#!/usr/bin/env python3
import os
from flask import Flask, request, render_template_string, render_template
from os import popen

app = Flask(__name__)

app.config['SECRET_SSTI_FLAG'] = 'flag={ssti_vuln_flask}'

def rp(command):
    return popen(command).read()


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/ping', methods=['POST', 'GET'])
def ping():
    address = None
    result = None
    if request.method == 'POST':
        address = request.form['address']
        if address:
          result = rp("ping -c 2 " + address).replace('\n', '\n<br>')  
    return render_template('ping.html', result=result)

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    name = ''
    if request.method == 'POST':
        name = '<br>Hello %s!<br><br>' %(request.form['name'])

    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vulnerable Flask App</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='base.css') }}">
    </head>
    <body>
        <nav class="navbar">
        <a href="{{ url_for('home') }}">
            <button class="button">Home</button>
        </a>
        <a href="{{ url_for('ping') }}">
            <button class="button">Ping</button>
        </a>
        <a href="{{ url_for('hello') }}">
            <button class="button">Hello</button>
        </a>
          <a href="#">
            <button class="button">Link 4</button>
        </a>
          <a href="#">
            <button class="button">Link 5</button>
        </a>
          <a href="#">
            <button class="button">Link 6</button>
        </a>
    </nav>

    <!-- Main -->
    <main>
        <form action = "/hello" method = "POST">
            <p><h3>What is your name?</h3></p>
            <p><input type = 'text' name = 'name' class='input-field'/></p>
            <p><input type = 'submit' value = 'Submit' class='submit-button'/></p>
         </form>
          %s
    </main>
    <footer>
        <p>© 2024 Vulnerable Flask App</p>
    </footer>
    </body>
    </html>
    """ %(name)
    return render_template_string(template)






















if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

