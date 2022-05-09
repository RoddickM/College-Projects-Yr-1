import sqlite3  # imports the built-in module by python

conn = sqlite3.connect("sport.db")  # creates the file

'''
table is created below with its keys


ID is an integer, a primary key and cannot be null
FIRST_NAME is characters with a limit of 50 and cannot be null
LAST_NAME is characters with a limit of 50 and cannot be null
AGE is integers
FAV_SPORT is text
PLAY_SPORT is a boolean
'''

conn.execute(('''CREATE TABLE SPORT
(ID INT PRIMARY KEY NOT NULL,
FIRST_NAME CHAR(50) NOT NULL,
LAST_NAME CHAR(50) NOT NULL,
AGE INT,
FAV_SPORT TEXT,
PLAY_SPORT TEXT)
'''))

# print statement confirms the creation of the table
print("Table is created")
