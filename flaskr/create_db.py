import sqlite3

connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

#Queries - node passwords soon to be saved as HASHES

#All these commmands have been run once just to initally populate table
#command = """DROP TABLE users; """
# command = """CREATE TABLE IF NOT EXISTS users(email TEXT, password TEXT)"""
# cursor.execute("INSERT into users VALUES ('sullivanlouis0@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('cianmc@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('benpri@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('katiecrow@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('abbiedel@gmail.com', 'admin')""")
#cursor.execute("INSERT into users VALUES ('admin', 'admin')""")
#cursor.execute("SE")
#connection.commit()