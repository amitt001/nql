#!/usr/bin/env python3

import languageprocess.stopword
import re
import json

'''
SQLIZE the Normal query data to sql syntax
'''

###################################################
sqldict = {}

sqldict.setdefault('SELECT',['choose','take','find', 'select', 'elect', 'pick', 'get'])
sqldict.setdefault('CREATE',['make','build','create', 'design', 'form', 'setup', 'invent', 'establish', 'produce', 'initiate', 'generate', 'devise', 'concieve', 'new'])
sqldict.setdefault('INSERT',['insert','put','enter', 'include', 'set', 'fill', 'inject', 'in'])
sqldict.setdefault('VALUES', ['value', 'data', 'values'])
sqldict.setdefault('*', ['all', 'each'])
sqldict.setdefault('where', ['whose', 'where"s'])
sqldict.setdefault('FROM', ['from'])
sqldict.setdefault('DROP', ['delete', 'remove', 'drop'])
sqldict.setdefault('MORE THAN', ['more', 'greater', 'higher'])
sqldict.setdefault('LESS THAN', ['below', 'less', 'lower'])

create_template = ['CREATE', 'TABLE', '(', ')']
####################################################


def sqlize(qinput, sample = None):
    # log queries
    fobj = open('logs', 'a');
    fobj.write('Query: ' + qinput + '\n')
    data = languageprocess.stopword.stopwordremover(qinput)
    for i in data:      # sql word synonyms corrections
        for key, value in sqldict.items():
            if i.lower() in value:
                data[data.index(i)] = key
    
    #for single word databse internal queries
    length = len(data) 
    #data = ' '.join(data)
    if length > 2 or ('SELECT' in data or 'CREATE' in data):
        data = sqltokenize(data, sample)
    else:
        data = singlequery(data)
    data = ' '.join(data) 
    fobj.write('SQLized: ' + data + '\n\n') #logging
    fobj.close()
    return data

datatype = ['text', 'integer', 'varchar']


def sqltokenize(qinput, sample):
    '''rightnow doing it for create only
    '''
    if 'CREATE' in qinput:
        qinput.remove('CREATE')
        newinput = ['CREATE', 'TABLE', '(', ')']
        for ind,inp in enumerate(create_template):
            if inp == 'TABLE': 
                newinput.insert(ind+1, qinput[0])
            if inp == '(':
                for i in range(1,len(qinput)):
                    newinput.insert(-1,qinput[i]+',')
                newinput[-2] = newinput[-2].rstrip(',')

        # For CREATE query data type interpretation. user only need to eneter the sample input :)
        try:
            sample = sample.replace(',', '').split()
        except Exception as e:
            return ['ERROR: You need to input sample input... Please try again with sample input.']

        b = []
        # to determine the datatype of attributes
        for i in sample: 
            if i.replace('.','').isdigit(): # for the float cases
                b.append('INTEGER')
            elif i.isalpha():
                b.append('TEXT')
            else:
                b.append('TEXT')
        attrs = newinput[newinput.index('(')+1:-1]#get attributes from newdata
        for ind, attr in enumerate(attrs):
#            attr = attr.replace(',', '')
            newinput[newinput.index(attr)] = attr.replace(',','') + ' ' +  b[ind] + ',' 
        newinput[-2] = newinput[-2].rstrip(',') # remove last ','
        inpu = newinput
        return inpu

    elif 'SELECT' in qinput:
        try:
            qinput.remove('SELECT')
            qinput.remove('*')
        except:
            pass
        newinput = []
        newinput.insert(0, 'SELECT')
        newinput.insert(1, '*')
        newinput.insert(2, 'FROM')
        with open('languageprocess/words.json', 'r') as fobj:
            js = json.load(fobj)
        # to get the table name and values associated with table name key
        for ind, dat in enumerate(qinput):
            if js.get(dat, 0):
                newinput.insert(3, dat)
                values = js[dat]
                qinput.remove(dat)
                newinput.append('WHERE') # appen where in all cases in absence of condition use 1
        # to get where conditions
        flag = 0
        for ind, val in enumerate(qinput[:]): # even revresed(qinput) could be used
            try:
                if val in  values:
                    flag = 1
                    if 'MORE THAN' in qinput:
                        sign = ' >= '
                        qinput.remove('MORE THAN')
                    elif 'LESS THAN' in qinput:
                        sign = ' <= '
                        qinput.remove('LESS THAN')
                    else:
                        sign = ' = '
                    newinput.append(val + sign)
                    newinput.append('sql')
                    qinput.remove(val)
            except Exception as e:
                print(e)
                return ['ERROR: Maybe you need to submit new table info to Word.json']

        if not flag:
            newinput.append('1')
            return newinput
        # to get values
        try:
            lenth = len(qinput)
            for l in range(lenth):
                # to put quotes for alpha
                if qinput[l].isalpha():
                    newinput[newinput.index('sql')] = '"' + qinput[l] + '"' + ','
                else:
                    newinput[newinput.index('sql')] = qinput[l] + ','
        except:
            return ['ERROR: This table schema doesnt exists in "words.json" file']
        newinput[-1] = newinput[-1].rstrip(',')
        return newinput

    else:
        '''
        Rightnow considering else case as insert case
        '''
        data = qinput
#        data = qinput.split()
        data = insert_token(data)
        data.insert(0, 'INSERT INTO')
#        data = ''.join(data)
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
#            val.append(data[index+1])

            i, lnth = index+2, len(data)
            stri = ''
            # for multiple word insert statements
            while i < lnth and (data[i]) != '=':
                stri += data[i - 1] + ' '
                i += 1
            #this if for one word value of last column
            if i == lnth:
                stri += data[i-1]
            val.append(stri)
    # to remove spaces
    attr = tuple([i.strip() for i in attr])
    val = tuple([j.strip() for j in val])
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

def singlequery(data):
    '''For processing smqll length queries that doesn't need much processing
    *Some conditions may be of sql specific.*
    '''
    if len(data) < 1 or 'tables' in data[0]: #case when user chack tables with 'table' ***improve***
        data = "SELECT name FROM sqlite_master WHERE type='table'".split()
        return data
    elif 'schema' in data:
        return ['schema']
    elif 'DROP' in data:
        data.insert(data.index('DROP') + 1, 'TABLE' )
        return data
    return data

if __name__ == '__main__':
    data = 'choOSe or select o.r : find or elect'
    print('input data: ', data)
    data = sqlize(data)
    print(data)
