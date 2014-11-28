#!/usr/bin/env python3

import stringmatch


def select(data):
    seen = set()
    lst = []
    for word in data:
        lst.append(stringmatch.correct(word))

    
