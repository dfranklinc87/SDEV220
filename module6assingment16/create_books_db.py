import sqlite3

# Create (or open) the database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create the books table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
""")

conn.commit()
conn.close()

print("books.db created with books table.")
