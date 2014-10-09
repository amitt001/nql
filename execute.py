#!/usr/bin/env python3

import sqlite3

def execi(query):
    db = sqlite3.connect('db/nql.db') 
    cursor = db.cursor()
    #query = "CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)"

    try:
        cursor.execute(query)
        db.commit()
    except Exception as e:
        db.rollback()
        return e
    finally:
        db.close
 
if __name__ == '__main__':
     execi()
