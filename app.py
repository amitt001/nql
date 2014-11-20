#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect, session
import execute
import languageprocess1.sqlizer
import languageprocess1.tokenizer
import sys
import os

#specify what belongs to application
app= Flask(__name__.split('.')[0]) 

app.secret_key = os.urandom(10)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    '''application home page with search box'''

    if request.method == 'POST':
        query = request.form['filename']
        squery = languageprocess1.sqlizer.sqlize(query)
        s = execute.execi(squery)
        global quer 
        quer = squery
        if not s:
            result = "Executed Successfully:" + quer
            session['result'] = result
            return redirect(url_for('search', result=result))
        else:
            result = "Error: " + str(s)
            session['result'] = result
            return redirect(url_for('search', result=result))

#            return "ERROR executing: " + squery + " , ERROR: " + str(s)

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = request.args['result']
    result = session['result']
    return result

if __name__ == '__main__':
    app.debug = True
    app.run()
