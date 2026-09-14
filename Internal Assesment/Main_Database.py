import sqlite3
import os 
sqlitedata = sqlite3.connect(
        "Project_database.db"
)

sqlitedata.execute(""" \
CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INT, 
        category STR,
        Amount REAL,
        Item STR,
        Date DATE
)
""")

tables = sqlitedata.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
""")

print(tables.fetchall())

sqlitedata.close()