import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sql_app"
)

mycursor = mydb.cursor()

def register(username, password, email):
  mycursor.execute("SELECT * FROM test")
  entries = mycursor.fetchall()

  for entry in entries:
    if (username == entry[0]):
      ...

    if (email == entry[1]):
      ...

  sql = f"INSERT INTO test (user_name, password, email, expiry_date, creation_date) VALUES ('{username}', '{password}', '{email}', 'CURDATE()', 'CURDATE()')"
  mycursor.execute(sql)
  mydb.commit()

register("AndrewHughes", "Joseph197i3802", "a.hughes16@share.epsb.ca")

def login (username, password):
  mycursor.execute("SELECT * FROM test")
  entries = mycursor.fetchall()
  for entry in entries:
    if entry[0] == username and entry[2]== password:
      ...

def randomstr(length): # return a random str of length length
    ...

def generate_license(length, days): # use randomstr to create a license id, then insert it into the database and return the id to the user

    ...