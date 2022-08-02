import sqlite3

data = sqlite3.connect('mbox.sqlite')
dbhd = data.cursor()

dbhd.execute('DROP TABLE if EXISTS Counts')
dbhd.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#打开文件
fname = input('Enter: ')
with open(fname) as fh:
    for line in fh:
        if not line.startswith('From: '):
            continue
        word = line.split()[1]
        orgname = word.split('@')[1]
        dbhd.execute('SELECT count FROM Counts WHERE org = ?', (orgname,))
        row = dbhd.fetchone()#抓取一个元组
        if row is None:
            dbhd.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (orgname,))
        else:
            dbhd.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (orgname,))
        
data.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
for row in dbhd.execute(sqlstr):
    print(str(row[0]), row[1])
    
dbhd.close()

        
    
