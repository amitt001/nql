#!/usr/bin/env python3

import languageprocess1.creater
import sys

'''
test script to check stopword, normalize, tokenize scripts
'''

try:
    query = sys.argv[1]
except:
    query = "no query"
i = languageprocess1.creater.sqlize(query)

print(i)
