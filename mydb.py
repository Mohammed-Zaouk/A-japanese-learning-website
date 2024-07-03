import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",     
    user="kawtar",        
    passwd="mz2002mz@"    
)


cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE mydatabase') 

cursorObject.close()
dataBase.close()

print("Database created successfully!")
