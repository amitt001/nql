#!/usr/bin/env python3

import sqlite3
import json

'''
execute the normalized sql queries on database
'''

def execi(query):
    db = sqlite3.connect('db/nql.db') 
    cursor = db.cursor()

    try:
        if 'SELECT' in query:
            cursor.execute(query)
            all_rows = cursor.fetchall()
            if not all_rows: # when table is empty
                newq = query.split()
                table_name = newq[newq.index('FROM') + 1]
                query = "PRAGMA table_info(" + table_name + ")"
                cursor.execute(query)
                all_rows = cursor.fetchall()
            return all_rows
        elif 'schema' in query:
            query = "SELECT name,sql FROM sqlite_master WHERE type='table'"
            cursor.execute(query)
            schema = cursor.fetchall()
            return schema
        else:
            cursor.execute(query)
            oquery = query
            if 'CREATE' in query:
                print('************************************************************')# json data
                query = query.split()
                worddict = {}
                flag = 1
                for words in query:
                    if words.islower():
                        if flag == 1:
                            worddict.setdefault(words,[])
                            flag = 0
                            key = words
                        else:
                            worddict[key].append(words)
                print(worddict)
                fo = open('languageprocess1/words.json')
                js = json.load(fo)
                if not js.get(key):
                    #copy dict
                    z = js.copy()
                    z.update(worddict)
                    fo.close()
                    #dump json
                    fo = open('languageprocess1/words.json', 'w')
                    json.dump(z, fo, indent = 4)
            db.commit()
            return 'Successful with interpreted query as: ' + oquery
    except Exception as e:
        db.rollback()
        print(e)
        return e
    finally:
        db.close
 
if __name__ == '__main__':
     err = execi('create table amit(id integer primary key, name text)')
     print(err)
