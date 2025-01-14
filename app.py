#!/usr/bin/env python3
import os
from flask import Flask, request, render_template_string, render_template, make_response
from os import popen
import html
import sqlite3
app = Flask(__name__)

app.config['SECRET_SSTI_FLAG'] = 'flag={ssti_vuln_flask}'

def rp(command):
    return popen(command).read()

comments = []

DATABASE_NAME = 'breakdb'

DATABASE_TABLES = [
  {
        'table_name' : 'users',
        'columns': [
            {'name' : 'id', 'datatype' : 'integer', 'nullable': False},
            {'name' : 'username', 'datatype' : 'varchar(40)', 'nullable': True},
            {'name' : 'password', 'datatype' : 'varchar(40)', 'nullable': False},
             {'name' : 'is_admin', 'datatype' : 'boolean', 'nullable': False}
        ]
    },
    {
        'table_name' : 'secret_table',
        'columns' : [
            {'name' : 'flag', 'datatype' : 'varchar(100)', 'nullable': True}
        ]
    }
]
DATABASE_CONTENTS = {
    'users': [
        (1, 'admin', '12dasfe345', True),
        (2, 'user', 'password', False),
    ],
    'secret_table' : [
        ('flag={sql_injection_admin_access}')
    ]
}

query_build = lambda x: x + ';'
connection = sqlite3.connect(':memory:', check_same_thread=False)
connection.isolation_level = None # autocommit
cursor = connection.cursor()
list_tables_query = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
cursor.execute(list_tables_query)
existing_tables = [a[0].lower() for a in cursor.fetchall()]
for table in [a for a in DATABASE_TABLES if a['table_name'].lower() not in existing_tables]: # create missing tables
    inner = ', '.join([' '.join([ (lambda x : x if isinstance(x, str) else 'NULL' if x else 'NOT NULL')(a[b]) for b in ['name', 'datatype', 'nullable'] ]) for a in table['columns'] ])
    cursor.execute(query_build('CREATE TABLE {} ({})'.format(table['table_name'].lower(), inner)))
    if table['table_name'].lower() == 'secret_table':
        values = ", ".join([f"'{a}'" if isinstance(a, str) else str(a) for a in DATABASE_CONTENTS['secret_table']])
        cursor.execute(query_build('INSERT INTO {} (flag) VALUES ({})'.format(table['table_name'], values)))
    for data in DATABASE_CONTENTS[table['table_name']]: # insert data into table 
        if table['table_name'].lower() != 'secret_table':
            columns = ', '.join([a['name'] for a in table['columns']])
            values = ', '.join([(lambda x: str(x) if isinstance(x, int) else "'{}'".format(x.replace("'", "\\'")))(a) for a in data])
            cursor.execute(query_build('INSERT INTO {} ({}) VALUES ({})'.format(table['table_name'], columns, values)))





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
        name = '<br><strong>Hello %s!</strong><br><br>' %(request.form['name'])

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
          <a href="{{ url_for('login') }}">
            <button class="button">Login</button>
        </a>
          <a href="{{ url_for('evaluation') }}">
            <button class="button">Evaluation</button>
        </a>
          <a href="{{ url_for('comment') }}">
            <button class="button">Comments Section</button>
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




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
        cursor.execute(query_build(query))
        user = cursor.fetchone()
        
        if user and user[3]:
             cursor.execute(query_build("SELECT flag from secret_table LIMIT 1"))
             flag = cursor.fetchone()
             if flag:
              return render_template('login.html', flag=flag[0])
        elif user:
            flag = 'Login successful, but no sensitive data could be accessed'
            return render_template('login.html', flag=flag)
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)


@app.route('/evaluation', methods = ['POST', 'GET'])
def evaluation():
    expression = None
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        if expression:
            try:
                result = str(eval(expression)).replace('\n', '\n<br>')
            except Exception as e:
                result = str(e)
    return render_template('eval.html', result=result)


@app.route('/comment', methods=['GET','POST'])
def comment():
    if 'comment' in request.form:
        comment = request.form['comment']
        comments.append(comment)
    
    resp = make_response(render_template('comment.html', comments=comments))
    resp.set_cookie('09282asjdeonc', 'flag={xss_vuln_flask}')
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

