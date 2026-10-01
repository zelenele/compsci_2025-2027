import sqlite3
import datetime as datetime 
sqlitedata = sqlite3.connect(
        "Project_database.db"
)
def create_tables():   
    with sqlite3.connect("Project_database.db") as sqlitedata:
        sqlitedata.execute(""" \
    CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INTEGER PRIMARY KEY, 
        category STR,
        Amount REAL,
        Item STR,
        Date DATE
    )


        """)

    sqlitedata.execute("""\
CREATE TABLE IF NOT EXISTS Income (
        income_id INTEGER PRIMARY KEY,
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


def Expenses(category,Amount,Item):
    print("connecting to the database")
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    sqlitedata = sqlite3.connect("Project_database.db")
    print("connected to the database")
    print("inserting expense record")
    sqlitedata.execute("""\
        INSERT INTO Expenses(category,Amount,Item,date)
        VALUES(?,?,?,?)""",
        (category,Amount,Item,date))
    print("expense record inserted")
    print("closing database connection")
    sqlitedata.commit()
    sqlitedata.close()
    print("database connection closed")

def Income(Amount,Source):
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    sqlitedata = sqlite3.connect("Project_database.db")
    sqlitedata.execute("""\
        INSERT INTO Income(Amount,Source,2date)
        VALUES(?,?,?)""",
        (Amount,Source,date))
    sqlitedata.commit()
    sqlitedata.close()


def View_Expenses():
    sqlitedata = sqlite3.connect("Project_database.db")
    category = input (str("Enter the category to view expenses (if you want to view all expenses, enter 'all'): "))
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
    if cursor.rowcount == 0:
        print(f"No ID found == {expense_id}.")
    else:
        print(f"Expense ID == {expense_id} deleted successfully.")
    sqlitedata.close()

def Delete_Income(income_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("DELETE FROM Income WHERE income_id = ?", (income_id,))
    sqlitedata.commit()
    if cursor.rowcount == 0:
        print(f"No ID found == {income_id}.")
    else:
        print(f"Income ID == {income_id} deleted successfully.")
    sqlitedata.close()

def Update_Expenses(category, Amount, Item):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Expenses
        SET category = ?, Amount = ?, Item = ?
        WHERE expense_id = ?""",
        (category, Amount, Item))
    sqlitedata.commit()
    sqlitedata.close()
def Update_Income( category, Amount, Source):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Income
        SET category = ?, Amount = ?, Source = ?
        WHERE income_id = ?""",
        (category, Amount, Source))
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
        category = input("Enter expense category: ")
        try:
            Amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
            continue
        Item = input("Enter expense item: ")
        Expenses(category, Amount, Item)
        print("Expense added successfully.")
        continue

    elif choice == "2":
        try:
            Amount = float(input("Enter income amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
            continue
        if Amount <= 0:
            print("Income amount must be greater than zero, or be a number at all.")
        Source = input("Enter income source: ")
        Income(Amount, Source)
        print("Income added successfully.")
        continue
    elif choice == "3":
        expenses = View_Expenses()
        if expenses:
            print("\nExpenses:")
            for expense in expenses:
                print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Item: {expense[3]}, Date: {expense[4]}")
            continue
        else:
            print("No expenses found.")
        continue
    
    elif choice == "4":
        income = View_Income()
        if income:
            print("\nIncome:")
            for inc in income:
                print(f"ID: {inc[1]}, Amount: {inc[2]}, Source: {inc[3]}, Date: {inc[4]}")
                continue
        else:
            print("No income found.")
        continue        
    
    elif choice == "5":
        expense_id = input("Enter the expense ID to delete: ")
        Delete_Expenses(expense_id)
        continue
    
    elif choice == "6":
        income_id = input("Enter the income ID to delete: ")
        Delete_Income(income_id)
        continue
    
    elif choice == "7":
        print("Exiting the program.")
    break