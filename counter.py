import sqlite3


num_you_need= input('Number you need:')



conn = sqlite3.connect('memmory.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Finals')
cur.execute('CREATE TABLE Finals (final TEXT ,first TEXT, second TEXT, third TEXT)')

cur.execute('INSERT INTO Finals (final, first, second, third) VALUES (?, ?, ?, ?)', ('7','4','+','3'))
cur.execute('INSERT INTO Finals (final, first, second, third) VALUES (?, ?, ?, ?)', ('12','4','*','3'))
conn.commit()
print('Finals:')
cur.execute('SELECT final, first, second, third FROM Finals')
for row in cur:
	methods = row
	print(row)

#cur.execute('DELETE FROM Tracks WHERE plays < 100')



#################################
way = str()
for i in methods:
	way = way + i	
eval_way = eval(way)
##################################
print(eval_way)

cur.close()