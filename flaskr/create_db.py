import sqlite3

connection = sqlite3.connect("hse_data.db")
cursor = connection.cursor()

#Queries - node passwords soon to be saved as HASHES

#All these commmands have been run once just to initally populate table
# command = """DROP TABLE users; """
#
# cursor.execute("""DROP TABLE medicalrecords; """)
#cursor.execute("""CREATE TABLE IF NOT EXISTS medicalrecords(ppsno TEXT, fname TEXT, sname TEXT, DOB TEXT, gender TEXT, medical_history TEXT)""")
#cursor.execute("INSERT into medicalrecords VALUES ('119363083G', 'Louis', 'Sullivan', '16/05/2001', 'Male', 'Diabetes, Asthma' )""")
# cursor.execute("INSERT into users VALUES ('cianmc@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('benpri@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('katiecrow@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('abbiedel@gmail.com', 'admin')""")
# cursor.execute("INSERT into users VALUES ('admin', 'admin')""")
# # cursor.execute("SE")
# # connection.commit()

# # cursor.execute("ALTER TABLE users ALTER COLUMN")
# # cursor.execute("SE")
#connection.commit()