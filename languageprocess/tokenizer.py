#!/usr/bin/env python3

import re

'''
Tokenizes the string input coming from web app.
'''

def tokenize(text):
    data = text
    data = data.split(' ')
    for index,word in enumerate(data):  # for wo:rd, am,it etc cases
        if re.match('[a-z0-9]+(?i)\W+[a-z0-9]+(?i)', word):
            data[index] = word.replace(word, re.sub('\W+','',word))
    data = ' '.join(data)

#    data = data.replace('\n',',').replace('\t',',').replace('. ',',').replace('-',',').replace(':',',').replace('?',',').replace('/',',').replace('\\',',').replace('|',',').replace('{',',').replace(';',',').replace('}',',').replace('(',',').replace(')',',').replace(' ', ',').split(',')
    
    data = data.replace('\n','`').replace('\t','`').replace('-','`').replace(':','`').replace(';','`').replace('. ', '`').replace(' ', '`').split('`')


    data = filter(None, data)
    return list(data)

if __name__ == '__main__':
    data = "insert int:o amit (name) values ('aaa')"
    print(data)
    textlist = tokenize(data)
    textlist = [txt for txt in textlist]
    print(textlist)
