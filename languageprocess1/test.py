#!/usr/bin/env python3

import stopword
import sqlizer

'''
test script to check stopword, normalize, tokenize scripts
'''

# contains some natural language text with some special characters in middle of text and line, contains letter both in capiatl and small latters and attributes 

#query = 'enter INTO a table --amit ColUmNs (name) wit:h data ("zzz", "kaka")'
#query = 'capital of india with the least population'
#query = 'why don"t you make a table amit with 2 columns (id is a integer, name is text)'
query = 'ENTER (id, name) in amit with (2, "amu") as values'
#i = stopword.stopwordremover(query)

i = sqlizer.sqlize(query)

print(i)
