# string composition

import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()


cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
  CREATE TABLE table1 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s, %s);', (1, True))



# fetching results from table

cursor.execute('SELECT * from table1;')
result=cursor.fetchall()
print(result)
 # /ends

connection.commit()

connection.close()
cursor.close()