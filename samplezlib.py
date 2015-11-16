import sqlite3
import zlib

# open and query the database
conn = sqlite3.connect('messagestore.db') # database name abbreviated
c = conn.cursor
c.execute("select _id, fromAddress, datetime(dateSentMS/1000,
    'unixepoch', 'localtime'), datetime(dateReceivedMS/1000,
    'unixepoch', 'localtime'), case when body not Null then body
    else bodycompressed end from messages ")
rows = c.fetchall()

# interate through the rows and decompress the long messages
for row in rows:
    id, _from, sent, recv, body = row
    try:
        body = zlib.decompress(body)
    except:
        pass
    print('{}|{}|{}|{}|{}'.format(id, _from, sent, recv, body))
