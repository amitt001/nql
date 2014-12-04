#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect, session
import execute
import languageprocess1.creater
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
        query = request.form['query']
        sampleinput = None
        if request.form['input']:
            sampleinput = request.form['input']
        squery = languageprocess1.creater.sqlize(query, sampleinput)
        s = execute.execi(squery)
        global quer 
        quer = squery
        if s:
            result = str(s)
            session['result'] = result
            return redirect(url_for('search', result=result))
        else:
            result = str(s)
            session['result'] = result
            return redirect(url_for('search', result=result))

    return render_template('index.html', title='NQL')


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = request.args['result']
    result = session['result']
    print(result)
    return render_template('result.html', value=result)
#    print()
#    return render_template('result.html', value=result)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
