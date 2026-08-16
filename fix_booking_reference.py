import sqlite3
import os

# Get the path to the database file
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if the booking_reference column exists
cursor.execute("PRAGMA table_info(petapp_bookingmaster)")
columns = [col[1] for col in cursor.fetchall()]
print("Current columns in petapp_bookingmaster:", columns)

# Add the booking_reference column if it doesn't exist
if 'booking_reference' not in columns:
    print("Adding booking_reference column...")
    cursor.execute('''
    ALTER TABLE petapp_bookingmaster
    ADD COLUMN booking_reference varchar(20) NULL UNIQUE
    ''')
    print("Column added successfully!")
else:
    print("booking_reference column already exists.")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database update completed!") 