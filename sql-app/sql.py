import mysql.connector
import string
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sql_app"
)

mycursor = mydb.cursor()

def register(username, password, email, license):
  mycursor.execute("SELECT * FROM test")
  entries = mycursor.fetchall()

  for entry in entries:
    if (username == entry[0]):
      return "Username already in use"

    if (email == entry[1]):
      return "Email already in use"

  mycursor.execute("SELECT * FROM licenses")
  entries = mycursor.fetchall()

  for entry in entries:
    if license == entry[0] and entry[1] == 0:
      sql = f"INSERT INTO test (user_name, password, email, expiry_date, creation_date) VALUES ('{username}', '{password}', '{email}','CURDATE()', 'CURDATE()')"
      mycursor.execute(sql)
      mydb.commit()

      sql = f"UPDATE licenses SET used=1 WHERE id='{license}'"
      mycursor.execute(sql)
      mydb.commit()

      return "Registered"

  return "License does not exist"



def login (username, password):
  mycursor.execute("SELECT * FROM test")
  entries = mycursor.fetchall()
  for entry in entries:
    if entry[0] == username and entry[2]== password:
      ...

def randomstr(stringLength=10): # return a random str of length length
  license=string.ascii_uppercase
  return ''.join(random.choice(license) for i
    in range(stringLength))
#
def generate_license(len, days): # use randomstr to create a license id, then insert it into the database and return the id to the user
  id = randomstr(len)
  sql = f"INSERT INTO licenses (id, used, days) VALUES ('{id}', '0', '{days}')"
  mycursor.execute(sql)
  mydb.commit()

  return id