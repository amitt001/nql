#!/usr/bin/env python3

import stopword

'''
SQLIZE the Normal query data to sql syntax
'''

sqldict = {}

sqldict.setdefault('SELECT',['choose','take','find', 'select', 'elect', 'pick'])
sqldict.setdefault('CREATE',['make','build','create', 'design', 'form', 'setup', 'invent', 'establish', 'produce', 'start', 'initiate', 'generate', 'devise', 'concieve'])
sqldict.setdefault('INSERT',['insert','put','enter', 'include', 'set', 'fill', 'inject'])
sqldict.setdefault('VALUES', ['value', 'data', 'values'])

# specify more sql words

#sqldict.setdefault()
#sqldict.setdefault()
#sqldict.setdefault()
#sqldict.setdefault()

def sqlize(input):
    
    index = 0
    data = stopword.stopwordremover(input)
    
    for i in data:
        for key, value in sqldict.items():
            if i in value:
                data[data.index(i)] = key
    
    data = ' '.join(data)
    return data


if __name__ == '__main__':
    data = 'choOSe or select o.r : find or elect'
    print('input data: ', data)
    data = sqlize(data)
    print(data)
