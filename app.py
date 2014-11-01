#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect
import tokenizer
import execute
import languageprocess1.sqlizer
import languageprocess1.tokenizer
import sys

app= Flask(__name__.split('.')[0]) #specify what belongs to application
#app.config.from_envvar('NQL_SETTINGS', silent=True)

s = ''
quer = ''


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    global s

    if request.method == 'POST':
        query = request.form['filename']
        #squery = tokenizer.tokenize(query)
        squery = languageprocess1.sqlizer.sqlize(query)
        print(squery)
        s = execute.execi(squery)
        print(s)
        global quer 
        quer = squery
        if not s:
            return redirect(url_for('search'))
        else:
            return "ERROR executing: " + squery

    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    global s
    return "Executed Successfully:" + quer

if __name__ == '__main__':
    app.debug = True
    app.run()
