#!/usr/bin/env python3

'''
    correct words according to database from user input.
    flexible user input for table names attributes.
'''


def correct(word):
    fobj = open('words.txt')
    count = 0
    char = word
    lst = []
    for data in fobj.readlines():
        new = [i for i in data for j in char if i == j]
        if sorted(set(new)) == sorted(char):
            lst.append(data)
    return lst


if __name__ == '__main__':
    correct()
