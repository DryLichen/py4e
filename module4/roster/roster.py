# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 23:14:43 2021

@author: Sarah Cheung
"""

import sqlite3
import json

#新建数据库
conn = sqlite3.connect('roster.sqlite')
dbhd = conn.cursor()

dbhd.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    
    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        name TEXT UNIQUE);
    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE);
    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id))
''')

#分析json文件
fname = input('Enter file name: ')
with open(fname) as fh:
    data = fh.read()
    jhd = json.loads(data)
    #print(json.dumps(jhd, indent = 4))
    
#写入数据库
for item in jhd:
    name = item[0]
    title = item[1]
    role = item[2]
    
    dbhd.execute('''INSERT OR IGNORE INTO User(name) 
             VALUES (?)''',(name,))
    dbhd.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = dbhd.fetchone()[0]
    
    dbhd.execute('''INSERT OR IGNORE INTO Course(title) 
             VALUES (?)''',(title,))
    dbhd.execute('SELECT id FROM Course WHERE title = ?',(title,))
    course_id = dbhd.fetchone()[0]
    
    dbhd.execute('''INSERT OR REPLACE INTO Member
                 (user_id, course_id, role) VALUES (?,?,?)''',
                 (user_id, course_id, role))
    
    conn.commit()

dbhd.close()