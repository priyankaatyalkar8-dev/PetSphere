import sqlite3
import os

# Get the path to the database file
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='petapp_bookingmaster'")
    if cursor.fetchone():
        print("Found petapp_bookingmaster table")

        # First, let's backup the existing table data
        try:
            cursor.execute("SELECT * FROM petapp_bookingmaster")
            existing_bookings = cursor.fetchall()
            print(f"Backed up {len(existing_bookings)} existing bookings")

            # Rename the current table
            cursor.execute("ALTER TABLE petapp_bookingmaster RENAME TO petapp_bookingmaster_old")
            print("Renamed existing table to petapp_bookingmaster_old")
        except Exception as e:
            print(f"Error backing up or renaming table: {str(e)}")

    # Create the new table with the updated schema
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS petapp_bookingmaster (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            customerName varchar(100) NOT NULL,
            email varchar(254) NOT NULL,
            contact varchar(15) NOT NULL,
            address TEXT NOT NULL,
            pincode varchar(10) NOT NULL,
            pet_name varchar(100) NOT NULL,
            pet_type varchar(50) NOT NULL,
            pet_breed varchar(100) NULL,
            pet_age INTEGER NULL,
            location_id INTEGER NULL REFERENCES petapp_boardinglocation(id),
            kennel_id INTEGER NULL REFERENCES petapp_kennel(id),
            check_in_date date NOT NULL,
            check_out_date date NOT NULL,
            booking_status varchar(20) NOT NULL DEFAULT 'Confirmed',
            booking_reference varchar(20) NULL UNIQUE,
            total_amount decimal(10, 2) NOT NULL DEFAULT 0,
            payment_method varchar(50) NOT NULL DEFAULT 'Cash',
            is_paid bool NOT NULL DEFAULT 0,
            created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        print("Created new BookingMaster table with updated schema")
    except Exception as e:
        print(f"Error creating new table: {str(e)}")

    # Verify the table structure
    cursor.execute("PRAGMA table_info(petapp_bookingmaster)")
    columns = cursor.fetchall()
    print("New table columns:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database update completed!")
except Exception as e:
    print(f"An error occurred: {str(e)}") 