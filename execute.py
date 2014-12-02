#!/usr/bin/env python3

import sqlite3

'''
execute the normalized sql queries on database
'''

def execi(query):
    db = sqlite3.connect('db/nql.db') 
    cursor = db.cursor()
    #query = "CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)"

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
        elif query == 'schema':
            query = "SELECT name,sql FROM sqlite_master WHERE type='table'"
            cursor.execute(query)
            schema = cursor.fetchall()
            return schema
        else:
            cursor.execute(query)
            return 'Successful with interpreted query as: ' + query
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        return e
    finally:
        db.close
 
if __name__ == '__main__':
     err = execi('create table amit(id integer primary key, name text)')
     print(err)
