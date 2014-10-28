#!/usr/bin/env python3

import languageprocess1.stopword

'''
SQLIZE the Normal query data to sql syntax
'''

sqldict = {}

sqldict.setdefault('SELECT',['choose','take','find', 'select', 'elect', 'pick'])
sqldict.setdefault('CREATE',['make','build','create', 'design', 'form', 'setup', 'invent', 'establish', 'produce', 'initiate', 'generate', 'devise', 'concieve', 'new'])
sqldict.setdefault('INSERT',['insert','put','enter', 'include', 'set', 'fill', 'inject', 'in'])
sqldict.setdefault('VALUES', ['value', 'data', 'values'])

# specify more sql syntax
sqldict.setdefault('*', ['all', 'each'])
sqldict.setdefault('where', ['whose', 'where"s'])
#sqldict.setdefault()
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
    fobj.write('SQLized: ' + data + '\n\n')
    fobj.close()
    return data

datatype = ['text', 'integer']

def sqltokenize(qinput):

#    data = qinput.replace('(','`').replace(')', '`').replace(',', '`').split('`')
    if "CREATE" in qinput:
        data = qinput.split()
        for index, value in enumerate(data):
            if 'table' in value:
                ind = data.index(value) 
                data[ind+2] = '(' + data[ind+2] 
            if 'integer' in value or 'text' in value:
                data[index] = data[index] + ','

        data = ' '.join(data)
        data = data.rstrip(',') + ')'

        return data

    elif "SELECT" in qinput:
        data = qinput.split()
        for index, value in enumerate(data):
            if 'table' in value:
                data.pop(index)
        data = ' '.join(data)
        return data
    return qinput


if __name__ == '__main__':
    data = 'choOSe or select o.r : find or elect'
    print('input data: ', data)
    data = sqlize(data)
    print(data)
