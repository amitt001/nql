#!/usr/bin/env python3

import stopword

'''
test script to check stopword, normalize, tokenize scripts
'''

# contains some natural language text with some special characters in middle of text and line, contains letter both in capiatl and small latters and attributes 

query = 'insert INTO a table amit ColUmNs (name) wit:h values ("zzz", "kaka")'

i = stopword.stopwordremover(query)

print(i)
