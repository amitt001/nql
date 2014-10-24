#!/usr/bin/env python3

#from languageprocess import stopword
#from languageprocess import sqlizer
import languageprocess1.sqlizer
import languageprocess1.tokenizer
import sys

'''
test script to check stopword, normalize, tokenize scripts
'''

# contains some natural language text with some special characters in middle of text and line, contains letter both in capiatl and small latters and attributes 

#query = 'enter INTO a table --amit ColUmNs (name) wit:h data ("zzz", "kaka")'
#query = 'capital of india with the least population'
#query = 'why don"t you make a table amit with 2 columns (id is a integer, name is text)'
try:
    query = sys.argv[1]
except:
    query = "new tab;le amit with 3 columns 'id integer' 'name text' 'class text'"
#i = stopword.stopwordremover(query)
#i = languageprocess1.tokenizer.tokenize(query)
i = languageprocess1.sqlizer.sqlize(query)

print(i)
