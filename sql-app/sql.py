import mysql.connector
import string
import random

import user

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
      sql = f"INSERT INTO test (user_name, password, email) VALUES ('{username}', '{password}', '{email}')"
      mycursor.execute(sql)
      mydb.commit()

      sql = f"UPDATE licenses SET used=1 WHERE id='{license}'"
      mycursor.execute(sql)
      mydb.commit()

      return "Registered"

  return "License does not exist"



def login(username, password):
  mycursor.execute("SELECT * FROM test")
  entries = mycursor.fetchall()
  for entry in entries:
    if entry[0] == username and entry[2]== password:

      user.admin = entry[4]
      return "Logged in"

  return "Username/password incorrect"

def randomstr(stringLength=10): # return a random str of length length
  license=string.ascii_uppercase
  return ''.join(random.choice(license) for i
    in range(stringLength))
#
def generate_license(len): # use randomstr to create a license id, then insert it into the database and return the id to the user
  id = randomstr(len)
  sql = f"INSERT INTO licenses (id, used) VALUES ('{id}', '0')"
  mycursor.execute(sql)
  mydb.commit()

  return id

def delete_all_users():
  sql = f"DELETE FROM test WHERE admin = 0"
  mycursor.execute(sql)
  mydb.commit()