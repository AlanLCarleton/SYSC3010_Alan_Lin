#!/usr/bin/env python3
import sqlite3
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

todayDate = str(datetime.today().strftime('%Y-%m-%d'))
nowTime = str(datetime.now().time().strftime('%H:%M:%S'))
temperature = round(sense.get_temperature())
for i in range(10):
    #execute insert statement
    cursor.execute('''insert into temps values (?, ?, ?, ?)''',
    (todayDate, nowTime, 'garage', temperature));

dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );
#close the connection
dbconnect.close();