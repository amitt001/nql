#!/usr/bin/env python3

'''
Tokenizes the string input coming from web app.
'''

def tokenize(text):
    data = text
    data = data.replace('\n',',').replace('\t',',').replace('. ',',').replace('-',',').replace(':',',').replace('?',',').replace('/',',').replace('\\',',').replace('|',',').replace('{',',').replace(';',',').replace('}',',').replace('(',',').replace(')',',').replace(' ', ',').split(',')
    data = filter(None, data)
    return list(data)

if __name__ == '__main__':
    data = "table city with fields id to recognize, city, country"
    print(data)
    textlist = tokenize("table city with fields id to recognize, city, country")
    textlist = [txt for txt in textlist]
    print(textlist)
