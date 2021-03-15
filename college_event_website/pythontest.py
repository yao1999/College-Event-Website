import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
#get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Universities.Unive' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==1 : 
	print('Table exists.')
else :
	print('Table does not exist.')
			
#commit the changes to db			
conn.commit()
#close the connection
conn.close()

# # delete all rows from table
# c.execute('DELETE FROM Universities;',)

# print('We have deleted', c.rowcount, 'records from the table.')

# #commit the changes to db			
# conn.commit()
# #close the connection
# conn.close()

  
