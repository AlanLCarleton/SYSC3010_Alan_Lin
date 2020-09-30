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

#Create 'temps' table if not existing
cursor.execute('''CREATE TABLE IF NOT EXISTS temps (tdate DATE, ttime TIME, zone TEXT, temperature NUMERIC);''')
dbconnect.commit();
todayDate = str(datetime.today().strftime('%Y-%m-%d')) #get today's date
nowTime = str(datetime.now().time().strftime('%H:%M:%S')) #get now time
temperature = round(sense.get_temperature()) #get temperature from SENSE HAT
rooms = ['kitchen', 'greenhouse', 'garage'] #some rooms to use
for i in range(9):
    #execute insert statement
    cursor.execute('''insert into temps values (?, ?, ?, ?)''',
    (todayDate, nowTime, rooms[i%3], temperature));
dbconnect.commit();

#Create new 'sensor' table if not existing
cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (sensorID NUMERIC, type TEXT, zone TEXT);''')
dbconnect.commit();
#execute insert statement
cursor.execute('''insert into sensors values (1, 'door', 'kitchen')''');
cursor.execute('''insert into sensors values (2, 'temperature', 'kitchen')''');
cursor.execute('''insert into sensors values (3, 'door', 'garage')''');
cursor.execute('''insert into sensors values (4, 'motion', 'garage')''');
cursor.execute('''insert into sensors values (5, 'temperature', 'garage')''');
dbconnect.commit();

#execute select statement for all data in 'temps'
cursor.execute('SELECT * FROM temps');
print("----------PRINTING ALL DATA FROM 'temps' TABLE----------")
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );
    
#execute select statement all sensors from kitchen in 'sensors'
cursor.execute("SELECT * FROM sensors WHERE zone = 'kitchen'");
print("\n----------DISPLAYING ALL DATA FROM 'sensors' IN 'kitchen'----------")
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
    
#execute select statement all door sensors in 'sensors'
cursor.execute("SELECT * FROM sensors WHERE type = 'door'");
print("\n----------DISPLAYING ALL 'door' sensor DATA FROM 'sensors'----------")
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
    
#close the connection
dbconnect.close();