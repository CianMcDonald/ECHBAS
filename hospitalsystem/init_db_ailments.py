import sqlite3

connection = sqlite3.connect("ailments.db")
cursor = connection.cursor()
cursor.execute("""DROP TABLE ailment; """)
connection.commit
# init db
# cursor.execute("""CREATE TABLE IF NOT EXISTS ailments(name TEXT, score INTEGER)""")
# cursor.execute("INSERT into ailments (name, score) VALUES ('airway compromise', 1),('Inadequate breathing', 1), ('Exsanguinating haemorrhage', 1), ('Currently seizing', 1), ('Abnormal age-related vital signs', 1), ('GCS ≤ 12', 1), ('Oxygen saturations ≤ 90%', 1), ('Severe pain (pain score 7-10)', 2), ('Uncontrollable major haemorrhage', 2), ('GCS 13 or 14', 2), ('Signs of compensated shock', 2), ('Oxygen saturations ≤ 92%', 2), ('Moderate pain (pain score 4-6)', 3), ('Uncontrollable minor haemorrhage', 3), ('History of unconsciousness', 3), ('Mild pain (Pain score 1-3)', 4), ('Problem <48 hours', 4), ('Problem > 48 hours', 5)")
# connection.commit()

