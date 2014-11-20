#!/usr/bin/env python3

import languageprocess1.stopword
import re

'''
SQLIZE the Normal query data to sql syntax
'''

sqldict = {}

sqldict.setdefault('SELECT',['choose','take','find', 'select', 'elect', 'pick', 'get'])
sqldict.setdefault('CREATE',['make','build','create', 'design', 'form', 'setup', 'invent', 'establish', 'produce', 'initiate', 'generate', 'devise', 'concieve', 'new'])
sqldict.setdefault('INSERT',['insert','put','enter', 'include', 'set', 'fill', 'inject', 'in'])
sqldict.setdefault('VALUES', ['value', 'data', 'values'])

# specify more sql syntax
sqldict.setdefault('*', ['all', 'each'])
sqldict.setdefault('where', ['whose', 'where"s'])
#sqldict.setdefault('FROM', ['from'])
#sqldict.setdefault()


def sqlize(qinput):
    # log queries
    fobj = open('logs', 'a');
    fobj.write('Query: ' + qinput + '\n')

    data = languageprocess1.stopword.stopwordremover(qinput)
    for i in data:
        for key, value in sqldict.items():
            if i.lower() in value:
                data[data.index(i)] = key
    
    data = ' '.join(data)
    data = sqltokenize(data)
    fobj.write('SQLized: ' + data + '\n\n') #logging
    fobj.close()

    return data

datatype = ['text', 'integer', 'varchar']


def sqltokenize(qinput):
    
    '''
    To formet the SQL query by putting brackets and quotes
    '''

    if 'CREATE' in qinput:
        data = qinput.split()
        data = create_check(data)
        for index, value in enumerate(data):
            if 'table' in value:
                ind = data.index(value) 
                data[ind+2] = '( ' + data[ind+2] 
            if 'integer' in value or 'text' in value:
                data[index] = data[index] + ','
        data = ' '.join(data)
        data = data.rstrip(',') + ' )'
        return data

    elif 'SELECT' in qinput or 'from' in qinput:
        data = qinput.split()
        for index, value in enumerate(data):
            if 'table' in value:
                data.pop(index)
        if '=' not in data and 'where' in data:  # for where case
            data.insert(-1, '=')
        if not data[-1].isdigit():
            data[-1] = '"' + data[-1] + '"'
        data = sqltemplate(data)
        data = ' '.join(data)
        return data

    else:
        '''
        Rightnow considering else case as insert case
        '''

        data = qinput.split()
        data = insert_token(data)
        data.insert(0, 'INSERT INTO')
        data = ' '.join(data)
        return data
    return qinput


def insert_token(qinput):
    '''
    for proper formatting of the insert queries i.e. quotes and commas
    '''
    attr = []
    val = []
    newdata = []
    data = qinput
    length = len(data) - 1 #index starts with 0
    for index,word in enumerate(data):
        if word == '=': #and index+1 != length: # last check to correct last ','
            attr.append(data[index-1])
            val.append(data[index+1])
    attr,val = tuple(attr), tuple(val)
    newdata = [data[0]]
    newdata.append(str(attr))
    newdata.append('VALUES')
    newdata.append(str(val))
    return newdata

def sqltemplate(data):

    '''sql query template: Correct the order of sql words. Last step of normalization
       try: Check if "SELECT" is  not in string except: "SELECT" is in string but not at the index 0
    '''

    if data[0] != 'SELECT' and ('from' in data or 'where' in data):
        try:
            del(data[data.index('SELECT')])
            data.insert(0, 'SELECT')
            return data
        except:
            data.insert(0, 'SELECT')
            return data
    return data


def create_check(data):
    
    '''
    check the correct sequence of the CREATE query
    '''
    
    if 'table' not in data:
        data.insert(1, 'table')
    return data


if __name__ == '__main__':
    data = 'choOSe or select o.r : find or elect'
    print('input data: ', data)
    data = sqlize(data)
    print(data)
