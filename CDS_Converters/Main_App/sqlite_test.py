import sqlite3

# Open a connection to the database
# conn = sqlite3.connect('mydatabase.db')
# /home/baboo.lal/BEYOND/CDS_Converters/db.sqlite3
conn = sqlite3.connect('/home/baboo.lal/BEYOND/CDS_Converters/db.sqlite3')
# Read the file
# with open('file.pdf', 'rb') as file:
#     file_data = file.read()

# Insert the file data into the database
# conn.execute('INSERT INTO files (data) VALUES (?)', [sqlite3.Binary(file_data)])


conn.execute('''INSERT INTO area(ACCURACY, POINTS, NAME) VALUES( 
90.5, 15, 'Kadanes Algo');''') 

# Commit the transaction
conn.commit()

# Close the connection
conn.close()