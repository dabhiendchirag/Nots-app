import sqlite3

conn = sqlite3.connect("toys_dy.db")
cur = conn.cursor()

# Pehle ensure karo table exist karta hai
cur.execute("""
CREATE TABLE IF NOT EXISTS toys (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    seller TEXT NOT NULL,
    created TEXT NOT NULL,
    updated DATETIME NOT NULL
)
""")

# Data insert karo
payload = {
    "name": "tedy bear",
    "description": "this is my favorite toys but i want to sell.", 
    "price": 200.00,
    "seller": "dabhi",
    "created": "2025-08-15",
    "updated": "2025-10-10 23:59:59"
}

cur.execute("""
INSERT INTO toys(name, description, price, seller, created, updated)
VALUES (?, ?, ?, ?, ?, ?)
""", tuple(payload.values()))

conn.commit()
conn.close()

print("Table ensured & data inserted successfully!")