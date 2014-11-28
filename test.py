#!/usr/bin/env python3

import languageprocess1.sqlizer
import sys

'''
test script to check stopword, normalize, tokenize scripts
'''

try:
    query = sys.argv[1]
except:
    query = "new tab;le amit with 3 columns 'id integer' 'name text' 'class text'"
i = languageprocess1.sqlizer.sqlize(query)

print(i)
