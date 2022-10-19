print('Content-Type: text/html\n')
#imports
import cgi
import cgitb; cgitb.enable()
import sqlite3


# Set up connection to database
db = sqlite3.connect("surreget_song_database.db")
cursor = db.cursor()

cursor.execute('''DROP TABLE IF EXISTS custom''')


# Save and close
db.commit()
db.close()