#!/usr/bin/env python3

import languageprocess.sqlizer
import sys

'''
test script to check stopword, normalize, tokenize scripts
'''

try:
    query = sys.argv[1]
except:
    query = "no query"
i = languageprocess.sqlizer.sqlize(query)

print(i)
