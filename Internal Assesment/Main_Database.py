import sqlite3
import datetime as datetime 
sqlitedata = sqlite3.connect(
        "Project_database.db"
)
def create_tables():   
    with sqlite3.connect("Project_database.db") as sqlitedata:
        sqlitedata.execute(""" \
    CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INT, 
        category STR,
        Amount REAL,
        Item STR,
        Date DATE
    )


        """)

    sqlitedata.execute("""\
CREATE TABLE IF NOT EXISTS Income (
        income_id INT,
        category STR,
        Amount REAL,
        Source STR,
        date DATE
        )
    """)
    tables = sqlitedata.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table'
    """)
create_tables()


def Expenses(id,category,Amount,Item):
    print("connecting to the database")
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    sqlitedata = sqlite3.connect("Project_database.db", isolation_level=None)
    print("connected to the database")
    print("inserting expense record")
    sqlitedata.execute("""\
        INSERT INTO Expenses(expense_id,category,Amount,Item,date)
        VALUES(?,?,?,?,?)""",
        (id,category,Amount,Item,date))
    print("expense record inserted")
    print("closing database connection")
    sqlitedata.commit()
    sqlitedata.close()
    print("database connection closed")

def Income(id,category,Amount,Source):
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    sqlitedata = sqlite3.connect("Project_database.db")
    sqlitedata.execute("""\
        INSERT INTO Income(income_id,category,Source,Amount,date)
        VALUES(?,?,?,?,?)""",
        (id,category,Source,Amount,date))
    sqlitedata.commit()
    sqlitedata.close()


def View_Expenses():
    sqlitedata = sqlite3.connect("Project_database.db")
    category = input (str("Enter the category to view expenses: "))
    cursor = sqlitedata.cursor()
    if category.lower() == "all":
        cursor.execute("SELECT * FROM Expenses")
    else:
        cursor.execute("SELECT * FROM Expenses WHERE category = ?", (category,))
    rows = cursor.fetchall()
    sqlitedata.close()
    return rows

def View_Income():
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("SELECT * FROM Income")
    rows = cursor.fetchall()
    sqlitedata.close()
    return rows

def Delete_Expenses(expense_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("DELETE FROM Expenses WHERE expense_id = ?", (expense_id,))
    sqlitedata.commit()
    sqlitedata.close()

def Delete_Income(income_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("DELETE FROM Income WHERE income_id = ?", (income_id,))
    sqlitedata.commit()
    sqlitedata.close()

def Update_Expenses(expense_id, category, Amount, Item):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Expenses
        SET category = ?, Amount = ?, Item = ?
        WHERE expense_id = ?""",
        (category, Amount, Item, expense_id))
    sqlitedata.commit()
    sqlitedata.close()
def Update_Income(income_id, category, Amount, Source):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Income
        SET category = ?, Amount = ?, Source = ?
        WHERE income_id = ?""",
        (category, Amount, Source, income_id))
    sqlitedata.commit()
    sqlitedata.close()

while True:

    print("\n Budget Tracker")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. View Income")
    print("5. Delete Expense")
    print("6. Delete Income")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter expense ID: ")
        category = input("Enter expense category: ")
        Amount = float(input("Enter expense amount: "))
        Item = input("Enter expense item: ")
        Expenses(id, category, Amount, Item)
        print("Expense added successfully.")