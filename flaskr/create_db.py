import sqlite3

connection = sqlite3.connect("hse_data.db")
#connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()

#Queries - node passwords soon to be saved as HASHES

#populate users login table
#email password, pps, fname, sname
#cursor.execute("INSERT into users VALUES ('ab@gmail.com', 'admin', '119470426B', 'Abbie', 'Delaney')""")
#cursor.execute("INSERT into users VALUES ('ls@gmail.com', 'admin', '119363083C', 'Louis', 'Sullivan')""")
#cursor.execute("INSERT into users VALUES ('bp@gmail.com', 'admin', '119372426D', 'Ben', 'Prizeman')""")
#cursor.execute("INSERT into users VALUES ('cd@gmail.com', 'admin', '119363843E', 'Cian', 'McDonald')""")
#cursor.execute("INSERT into users VALUES ('kc@gmail.com', 'admin', '119363843F', 'Katie', 'Crowdle')""")




#cursor.execute("DELETE FROM medicalrecords WHERE ppsno = '119363083C'")
#cursor.execute("""CREATE TABLE IF NOT EXISTS medicalrecords(ppsno TEXT, fname TEXT, sname TEXT, DOB TEXT, gender TEXT, medical_history TEXT)""")
# cursor.execute("INSERT into medicalrecords VALUES ('123A', 'Admin', 'Admin', '01/01/1990', 'Other', 'None' )""")
# cursor.execute("INSERT into medicalrecords VALUES ('119470426B', 'Abbie', 'Delaney', '01/09/2000', 'Female', 'Diabetes, Asthma' )""")
#cursor.execute("INSERT into medicalrecords VALUES ('119363083C', 'Louis', 'Sullivan', '16/05/2001', 'Male', 'Sniffles' )""")
# cursor.execute("INSERT into medicalrecords VALUES ('119372426D', 'Ben', 'Prizeman', '23/02/2001', 'Male', 'Haemorrhoids' )""")
# cursor.execute("INSERT into medicalrecords VALUES ('119363843E', 'Cian', 'McDonald', '20/03/2001', 'Male', 'Balding' )""")
# cursor.execute("INSERT into medicalrecords VALUES ('119363843F', 'Katie', 'Crowdle', '20/07/2000', 'Female', 'Coeliac' )""")
connection.commit()



"""
Louis Sullivan	119363083
Ben Prizeman	119372426
Abbie Delaney	119470426
Katie Crowdle	119325941
Cian McDonald	119363843
"""