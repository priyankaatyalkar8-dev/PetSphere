import sqlite3
import os

# Get the path to the database file
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if the necessary tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [table[0] for table in cursor.fetchall()]
print("Existing tables:", tables)

# Create the tables if they don't exist
if 'petapp_boardinglocation' not in tables:
    print("Creating petapp_boardinglocation table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "petapp_boardinglocation" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name" varchar(100) NOT NULL,
        "image" varchar(100) NULL,
        "description" text NULL
    );
    ''')
    
    # Insert sample data
    cursor.execute('''
    INSERT INTO "petapp_boardinglocation" ("name", "description")
    VALUES ('Downtown Pet Hotel', 'Modern facility in the heart of the city with 24/7 care and monitoring.');
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_boardinglocation" ("name", "description")
    VALUES ('Suburban Pet Resort', 'Spacious outdoor play areas and comfortable indoor accommodations.');
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_boardinglocation" ("name", "description")
    VALUES ('Luxury Pet Palace', 'Premium boarding experience with private suites and personalized care.');
    ''')

if 'petapp_kennel' not in tables:
    print("Creating petapp_kennel table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "petapp_kennel" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name" varchar(100) NOT NULL,
        "is_active" bool NOT NULL,
        "location_id" integer NOT NULL REFERENCES "petapp_boardinglocation" ("id") DEFERRABLE INITIALLY DEFERRED
    );
    ''')
    
    # Insert sample data for kennels - Downtown Pet Hotel (location_id = 1)
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Standard Suite 1', 1, 1);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Standard Suite 2', 1, 1);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Deluxe Suite 1', 1, 1);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Premium Suite 1', 1, 1);
    ''')
    
    # Insert sample data for kennels - Suburban Pet Resort (location_id = 2)
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Cozy Cabin 1', 1, 2);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Cozy Cabin 2', 1, 2);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Garden View 1', 1, 2);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Garden View 2', 1, 2);
    ''')
    
    # Insert sample data for kennels - Luxury Pet Palace (location_id = 3)
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Royal Suite 1', 1, 3);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Royal Suite 2', 1, 3);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('Presidential Suite', 1, 3);
    ''')
    
    cursor.execute('''
    INSERT INTO "petapp_kennel" ("name", "is_active", "location_id")
    VALUES ('VIP Suite', 1, 3);
    ''')

if 'petapp_kennelbooking' not in tables:
    print("Creating petapp_kennelbooking table...")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "petapp_kennelbooking" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "check_in_date" date NOT NULL,
        "is_booked" bool NOT NULL,
        "kennel_id" integer NOT NULL REFERENCES "petapp_kennel" ("id") DEFERRABLE INITIALLY DEFERRED,
        UNIQUE ("kennel_id", "check_in_date")
    );
    ''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database tables created successfully!") 