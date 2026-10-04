import sqlite3
import datetime as datetime 
import customtkinter as ctk
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
        INSERT INTO Income(Amount,Source,date)
        VALUES(?,?,?)""",
        (Amount,Source,date))
    sqlitedata.commit()
    sqlitedata.close()


def View_Expenses(category):
    sqlitedata = sqlite3.connect("Project_database.db")
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
    if cursor.rowcount == 1:
        result = True
    else:
        result = False
    
    sqlitedata.close()
    return result

def Delete_Income(income_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("DELETE FROM Income WHERE income_id = ?", (income_id,))
    sqlitedata.commit()
    if cursor.rowcount == 0:
        result = False
    else:
        result = True
    sqlitedata.close()
    return result

def Update_Expenses(category, Amount, Item, expense_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Expenses
        SET category = ?, Amount = ?, Item = ?
        WHERE expense_id = ?""",
        (category, Amount, Item, expense_id))
    sqlitedata.commit()
    sqlitedata.close()
def Update_Income( Amount, Source, income_id):
    sqlitedata = sqlite3.connect("Project_database.db")
    cursor = sqlitedata.cursor()
    cursor.execute("""\
        UPDATE Income
        SET  Amount = ?, Source = ?
        WHERE income_id = ?""",
        (Amount, Source, income_id))
    sqlitedata.commit()
    sqlitedata.close()



# while True:

#     print("\n Budget Tracker")
#     print("1. Add Expense")
#     print("2. Add Income")
#     print("3. View Expenses")
#     print("4. View Income")
#     print("5. Delete Expense")
#     print("6. Delete Income")
#     print("7. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         category = input("Enter expense category: ")
#         try:
#             Amount = float(input("Enter expense amount: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid number for the amount.")
#             continue
#         Item = input("Enter expense item: ")
#         Expenses(category, Amount, Item)
#         print("Expense added successfully.")
#         continue

#     elif choice == "2":
#         try:
#             Amount = float(input("Enter income amount: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid number for the amount.")
#             continue
#         if Amount <= 0:
#             print("Income amount must be greater than zero, or be a number at all.")
#         Source = input("Enter income source: ")
#         Income(Amount, Source)
#         print("Income added successfully.")
#         continue
#     elif choice == "3":
#         expenses = View_Expenses()
#         if expenses:
#             print("\nExpenses:")
#             for expense in expenses:
#                 print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Item: {expense[3]}, Date: {expense[4]}")
#             continue
#         else:
#             print("No expenses found.")
#         continue
    
#     elif choice == "4":
#         income = View_Income()
#         if income:
#             print("\nIncome:")
#             for inc in income:
#                 print(f"ID: {inc[1]}, Amount: {inc[2]}, Source: {inc[3]}, Date: {inc[4]}")
#                 continue
#         else:
#             print("No income found.")
#         continue        
    
#     elif choice == "5":
#         expense_id = input("Enter the expense ID to delete: ")
#         Delete_Expenses(expense_id)
#         continue
    
#     elif choice == "6":
#         income_id = input("Enter the income ID to delete: ")
#         Delete_Income(income_id)
#         continue
    
#     elif choice == "7":
#         print("Exiting the program.")
#     break

def Gui():
    root = ctk.CTk()
    
    
    def add_expense_window():
        window = ctk.CTkToplevel(root)
        window.title("Add Expense ")
        window.geometry("400x400")
        category = ctk.CTkEntry(window, placeholder_text="Category")
        category.pack(pady=10)
        amount = ctk.CTkEntry(window, placeholder_text="Amount")
        amount.pack(pady=10)
        item = ctk.CTkEntry(window, placeholder_text="Item")
        item.pack(pady=10)
        def add_button():
            Expenses(category.get(), amount.get(), item.get())
        add_expense_button = ctk.CTkButton(window, text="Add", command=add_button)
        add_expense_button.pack(pady=10)

    def add_income_window():
        window = ctk.CTkToplevel(root)
        window.title("Add Income")
        window.geometry("400x400")
        amount = ctk.CTkEntry(window, placeholder_text="Amount")
        amount.pack(pady=10)
        source = ctk.CTkEntry(window, placeholder_text="Source")
        source.pack(pady=10)
        def add_button():
            Income(amount.get(), source.get())
        add_income_button = ctk.CTkButton(window, text="Add", command=add_button)
        add_income_button.pack(pady=10)

    def view_expenses_window():
        window = ctk.CTkToplevel(root)
        window.title("View Expenses")
        window.geometry("400x400")
        expenses = ctk.CTkEntry(window, placeholder_text="enter expense category (if want to se all type 'all')")
        expenses.pack(pady=10)
        result_frame = ctk.CTkFrame(window)
        result_frame.pack(pady=10)
        def view_button():
            for widget in result_frame.winfo_children():
                widget.destroy()
            data = View_Expenses(expenses.get())
            
            if data:
                for expense in data:
                    ctk.CTkLabel(result_frame, text=f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Item: {expense[3]}, Date: {expense[4]}").pack(pady=5)
            else:
                ctk.CTkLabel(result_frame, text="No expenses found.").pack(pady=5)
        view_button = ctk.CTkButton(window, text="View expenses", command=view_button)
        view_button.pack(pady=10)
        

    def view_income_window():
        window = ctk.CTkToplevel(root)
        window.title("View Income")
        window.geometry("400x400")
        income = View_Income()
        if income:
            for inc in income:
                ctk.CTkLabel(window, text=f"ID: {inc[0]}, Amount: {inc[2]}, Source: {inc[3]}, Date: {inc[4]}").pack()
        else:
            ctk.CTkLabel(window, text="No income found.").pack()
    def delete_expense_window():
        window = ctk.CTkToplevel(root)
        window.title("Delete Expense")
        window.geometry("400x400")
        expense_id = ctk.CTkEntry(window, placeholder_text="Expense ID")
        expense_id.pack(pady=10)
        result_frame = ctk.CTkFrame(window)
        result_frame.pack(pady=10)
        def delete_expense():
            for widget in result_frame.winfo_children():
                widget.destroy()
            expense_found = Delete_Expenses(expense_id.get())
            if expense_found == True:
                ctk.CTkLabel(result_frame, text=f"Expense ID {expense_id.get()} deleted successfully.").pack(pady=5)
            else:
                ctk.CTkLabel(result_frame, text="No ID found.").pack(pady=5)

        delete_expense_button = ctk.CTkButton(window, text="Delete", command=delete_expense)
        delete_expense_button.pack(pady=10)
    
    def delete_income_window():
        window = ctk.CTkToplevel(root)
        window.title("Delete Income")
        window.geometry("400x400")
        income_id = ctk.CTkEntry(window, placeholder_text="Income ID")
        income_id.pack(pady=10)
        result_frame = ctk.CTkFrame(window)
        result_frame.pack(pady=2)
        def delete_income():
            income_found = Delete_Income(income_id.get())
            if income_found == True:
                ctk.CTkLabel(result_frame, text=f"Income ID {income_id.get()} deleted successfully.").pack(pady=5)
            else:
                ctk.CTkLabel(result_frame, text="No ID found.").pack(pady=5)

        delete_income_button = ctk.CTkButton(window, text="Delete", command=delete_income)
        delete_income_button.pack(pady=10)
    
    def update_expense_window():
        window = ctk.CTkToplevel(root)
        window.title("Update Expense")
        window.geometry("400x400")
        previous_id = ctk.CTkEntry(window,width= 300, placeholder_text="Id of the column you want to change")
        previous_id.pack(pady=10)
        category =  ctk.CTkEntry(window,width= 300, placeholder_text="New category")
        category.pack(pady=10)
        amount = ctk.CTkEntry(window,width= 300, placeholder_text="New amount")
        amount.pack(pady=10)
        item =  ctk.CTkEntry(window,width= 300, placeholder_text="New item")
        item.pack(pady=10)
        def update_expense():
            if previous_id.get() and category.get() and amount.get() and item.get():
                Update_Expenses(category.get(), amount.get(), item.get(), previous_id.get())
            else:
                ctk.CTkLabel(window, text="Please fill in all fields.").pack(pady=5)
        update_expense_button = ctk.CTkButton(window, text="Update", command=update_expense)
        update_expense_button.pack(pady=10)
    def update_income_window():
        window = ctk.CTkToplevel(root)
        window.title("Update Income")
        window.geometry("400x400")
        previous_id = ctk.CTkEntry(window,width= 300, placeholder_text="Id of the column you want to change")
        previous_id.pack(pady=10)
        source =  ctk.CTkEntry(window,width= 300, placeholder_text="New source")
        source.pack(pady=10)
        amount = ctk.CTkEntry(window,width= 300, placeholder_text="New amount")
        amount.pack(pady=10)
        def update_income():
            if previous_id.get() and source.get() and amount.get():
                Update_Income(amount.get(), source.get(), previous_id.get())
            else:
                ctk.CTkLabel(window, text="Please fill in all fields.").pack(pady=5)

        update_income_button = ctk.CTkButton(window, text="Update", command=update_income)
        update_income_button.pack(pady=10)

    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("green")

    
    root.title("\nBudget Tracker")
    root.geometry('1080x1080')

    title = ctk.CTkLabel(root, text="", font=("Arial", 24))
    title.pack(pady=30)

    title = ctk.CTkLabel(
        root,
        text="Budget Tracker",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=40)

    # Button implementation
    add_expense_button = ctk.CTkButton(
        root,
        text="Add Expense",
        width=250,
        height=50,
        command=add_expense_window
        
    )
    add_expense_button.pack(pady=10)

    add_income_button = ctk.CTkButton(
        root,
        text="Add Income",
        width=250,
        height=50,
        command=add_income_window
    )
    add_income_button.pack(pady=10)

    view_expenses_button = ctk.CTkButton(
        root,
        text="View Expenses",
        width=250,
        height=50,
        command=view_expenses_window
    )
    view_expenses_button.pack(pady=10)

    view_income_button = ctk.CTkButton(
        root,
        text="View Income",
        width=250,
        height=50,
        command=view_income_window
    )
    view_income_button.pack(pady=10)

    delete_expense_button = ctk.CTkButton(
        root,
        text="Delete Expense",
        width=250,
        height=50,
        command=delete_expense_window
    )
    delete_expense_button.pack(pady=10)

    delete_income_button = ctk.CTkButton(
        root,
        text="Delete Income",
        width=250,
        height=50,
        command=delete_income_window
    )
    delete_income_button.pack(pady=10)

    update_expense_button = ctk.CTkButton(
        root,
        text="Update Expense",
        width=250,
        height=50,
        command=update_expense_window
    )
    update_expense_button.pack(pady=10)

    update_income_button = ctk.CTkButton(
        root,
        text="Update Income",
        width=250,
        height=50,
        command=update_income_window
    )
    update_income_button.pack(pady=10)

    root.mainloop()
Gui()