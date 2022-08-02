import sqlite3
import xml.etree.ElementTree as ET

#链接数据库
conn = sqlite3.connect('music.sqlite')
dbhd = conn.cursor()

#建立表格
dbhd.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;            

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

#建立查找函数
def lookup(targ, word):
    found = False
    for i in targ:
        if found:
            return i.text
        if i.tag == 'key' and i.text == word:
            found = True
    return None
        
#分析xml
fname = input('Enter file name: ')
tree = ET.parse(fname)
subtree = tree.findall('dict/dict/dict')
for item in subtree:
    if lookup(item, 'Track ID') is None: 
        continue
    name = lookup(item, 'Name')
    genre = lookup(item, 'Genre')
    length = lookup(item, 'Total Time')
    rating = lookup(item, 'Rating')
    count = lookup(item, 'Play Count')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    if name is None or genre is None or album is None or artist is None:
        continue
    
#插入数据库
    dbhd.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)', (artist,))
    dbhd.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = dbhd.fetchone()[0]
    
    dbhd.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    dbhd.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = dbhd.fetchone()[0]
    
    dbhd.execute('INSERT OR IGNORE INTO Album(title, artist_id) VALUES (?, ?)', (album, artist_id))
    dbhd.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = dbhd.fetchone()[0]
    
    dbhd.execute('''
                 INSERT OR REPLACE INTO Track
                 (title, album_id, genre_id, len, rating, count) 
                 VALUES (?,?,?,?,?,?)''', (name, album_id, genre_id, length, rating, count))
    conn.commit()

dbhd.close()