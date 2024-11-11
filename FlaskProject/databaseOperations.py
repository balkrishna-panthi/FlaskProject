import sqlite3 as sql
from models import User

def getAllUsers():
    with sql.connect("Database.db") as connection:
        cur = connection.cursor()
        cur.execute('select * from users')
        rows = cur.fetchall()
        users = [
            User(first_name=row[1], middle_name=row[2], last_name=row[3], email=row[4], password=row[5], role=row[6])
            for row in rows
        ]
        for us in users:
            print(us.first_name)
        return users
    
def insertUserRecords(user : User):
     with sql.connect("Database.db") as connection:
        cur = connection.cursor()
        query = "INSERT INTO users (FirstName, MiddleName, LastName, Email, Password, Role) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, (user.first_name, user.middle_name, user.last_name, user.email, user.password, 0))
        connection.commit()
        #connection.close()
        #rows = cur.fetchall()

def getUserNameFromEmail(email):
     with sql.connect("Database.db") as connection:
        cur = connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = ?', (email,))
        row = cur.fetchone()
        name = row[1]
        return name
        