def setupCGI(dbName, out_file):
  with open(out_file, 'w') as f_out:
    script = '''#!/usr/bin/python
print('Content-type: text/html\\n\\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3\n\n'''
    script += f"mydb = '{dbName}'\n"
    script += '''conn = sqlite3.connect(mydb)
cursor = conn.cursor()\n\n'''
    f_out.write(script)


cursor.execute('''SELECT Title, Popularity
                FROM Song

''')
records = cursor.fetchall()


def closeCGI(out_file):
  with open(out_file, "a") as f_out:
    script = 'conn.commit()\ncursor.close()'
    f_out.write(script)
