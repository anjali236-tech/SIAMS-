import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="flask_user",
    password="password123",
    database="asset_management",
    charset="utf8"
)
cursor = conn.cursor()

# Table create
cursor.execute(
CREATE TABLE IF NOT EXISTS assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL
)
)


# Check if table is empty
cursor.execute("SELECT COUNT(*) FROM assets")
count = cursor.fetchone()[0]

# Insert default data agar empty hai
if count == 0:
    default_assets = [
        ('AC', 'available'),
        ('Projector', 'available'),
        ('Laptop', 'in use')
    ]
    cursor.executemany("INSERT INTO assets (name, status) VALUES (%s, %s)", default_assets)
    conn.commit()
    print("Default data inserted!")
else:
    print("Table already has data.")

# Data fetch
cursor.execute("SELECT * FROM assets")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()






