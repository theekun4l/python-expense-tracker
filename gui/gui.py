from files.storage import load_file
from tkinter import *
from tkinter import messagebox as tmsg
from files.income import add_income
from files.expenses import add_expense
from files.balance import balance,summary
from files.budget import set_budget,budget_status


expenses_dict = load_file("expenses.json")
salary_dict = load_file("salary.json")
budget_dict = load_file("budget.json")


def a_income():
    var1 = StringVar()
    var1.set("")
    var2 = StringVar()
    var2.set("")

    def income_extract():
        global salary_dict
        income = var1.get()
        source_name = var2.get()
        if income == "" or source_name == "":
            tmsg.showerror("Error", "Fill all fields")
            return
        if not income.isdigit():
            tmsg.showerror("Error", "Enter valid number!")
            return
        if source_name.isdigit():
            tmsg.showerror("Error", "Enter valid name!")
            return
        int_income = int(income)
        if int_income <= 0:
            tmsg.showerror("Error", "Enter valid number!")
            return
        else:
            salary_dict = add_income(salary_dict, int_income, source_name.lower())
            tmsg.showinfo("Success", "Income added!")
            var1.set("")
            var2.set("")
    window = Toplevel(root)
    window.geometry("500x500")
    window.title("Add Income")
    Label(window,text="Source Name: ",font="Helvetica 10 ").grid(row=0,column=0,pady=10,padx=10)
    Entry(window,textvariable=var2,width=40).grid(sticky="ew",row=0,column=1,pady=10,padx=10)
    Label(window,text="Income: ",font="Helvetica 10").grid(row=1,column=0,pady=10,padx=10)
    Entry(window,textvariable=var1,width=40).grid(sticky="ew",row=1,column=1,pady=10,padx=10)
    Button(window,text="Submit",command=income_extract).grid(row=2,column=1)
    Button(window,text="Exit",command=window.destroy).grid(row=5,column=1)

def a_expense():

    var1 = StringVar()
    var1.set("")
    var2 = StringVar()
    var2.set("")

    def extract_expenses():
        global expenses_dict
        expense = var1.get()
        source_name = var2.get()
        if expense == "" or source_name == "":
            tmsg.showerror("Error", "Fill all fields")
            return
        if not expense.isdigit():
            tmsg.showerror("Error", "Enter valid number!")
            return
        if source_name.isdigit():
            tmsg.showerror("Error", "Enter valid name!")
            return
        int_expense = int(expense)
        if int_expense <= 0:
            tmsg.showerror("Error", "Enter valid number!")
            return
        else:
            expenses_dict = add_expense(expenses_dict, int_expense, source_name.lower())
            tmsg.showinfo("Success", "Expense added!")
            var1.set("")
            var2.set("")

    window = Toplevel(root)
    window.geometry("500x500")
    window.title("Add Expenses")
    Label(window, text="Expense Source Name: ", font="Helvetica 10 ").grid(row=0, column=0, pady=10, padx=10)
    Entry(window, textvariable=var2, width=40).grid(sticky="ew", row=0, column=1, pady=10, padx=10)
    Label(window, text="Expense: ", font="Helvetica 10").grid(row=1, column=0, pady=10, padx=10)
    Entry(window, textvariable=var1, width=40).grid(sticky="ew", row=1, column=1, pady=10, padx=10)
    Button(window, text="Submit", command=extract_expenses).grid(row=2, column=1)
    Button(window, text="Exit", command=window.destroy).grid(row=5, column=1)
def check_balance():
    expense,salary = balance(salary_dict,expenses_dict)
    window = Toplevel(root)
    window.title("Balance")
    window.geometry("500x500")
    Label(window,text="-------Balance Summary------",font = "Helvetica 15 bold").grid(row=0,column=0,pady=10,padx=10)
    Label(window,text=f"Total Salary : {salary}",font="Helvetica 10").grid(row=1,column=0,pady=10,padx=10)
    Label(window, text=f"Total Expense : {expense}",font="Helvetica 10").grid(row=2, column=0, pady=10, padx=10)
    Label(window, text=f"Total Balance : {salary - expense}",font="Helvetica 10").grid(row=3, column=0, pady=10, padx=10)
    Button(window,text="Exit",command=window.destroy).grid(row=4, column=1,padx=10,pady=10)
def cat_summary():
    window = Toplevel(root)
    window.geometry("500x500")
    window.title("Category Summary")
    dict = summary(expenses_dict)
    Label(window,text="------Category Summary------",font="Helvetica 20 bold").grid(row=0,column=0,pady=10,padx=10)
    row = 0
    for key, value in dict.items():
        row = row + 1
        Label(window,text=f"{key.capitalize()} : {value}",font="Helvetica 15").grid(row=row,column=0,pady=10,padx=10)

    Button(window,text="Exit",command=window.destroy).grid(padx=10,pady=10)
def budget():
    var1 = StringVar()
    var1.set("")
    def budget_extract():
        global budget_dict
        user_budget = var1.get()
        if user_budget == "" :
            tmsg.showerror("Error", "Fill all fields")
            return
        if not user_budget.isdigit():
            tmsg.showerror("Error", "Enter valid number!")
            return
        int_budget = int(user_budget)
        if int_budget <= 0:
            tmsg.showerror("Error", "Enter valid number!")
            return
        else:
            budget_dict = set_budget(budget_dict,int_budget)
            tmsg.showinfo("Success", "Budget added!")
            var1.set("")
    window = Toplevel(root)
    window.geometry("500x500")
    window.title("Set Budget")
    Label(window, text="Budget: ", font="Helvetica 10").grid(row=1, column=0, pady=10, padx=10)
    Entry(window, textvariable=var1, width=40).grid(sticky="ew", row=1, column=1, pady=10, padx=10)
    Button(window, text="Submit", command=budget_extract).grid(row=2, column=1)
    Button(window, text="Exit", command=window.destroy).grid(row=5, column=1)
def budget_stat():
    window = Toplevel(root)
    window.geometry("500x500")
    window.title("Budget Status")
    result = budget_status(budget_dict,expenses_dict)
    if result:
        budget,total_expense,remaining = result
        Label(window,text="------Budget Status------",font="Helvetica 20 bold").grid(row=0,column=0,pady=10,padx=10)
        Label(window,text=f"Budget : {budget}",font="Helvetica 10").grid(row=1,column=0,pady=10,padx=10)
        Label(window,text=f"Total Expenses : {total_expense}",font="Helvetica 10").grid(row=2, column=0,pady=10,padx=10)
        Label(window,text=f"Remaining Budget : {remaining}",font="Helvetica 10").grid(row=3, column=0,pady=10,padx=10)
        Button(window,text="Exit",command=window.destroy).grid(row=4, column=1)
root = Tk()


root.title("Welcome")
root.geometry("500x500")
f1 = Frame(root,bd=3,relief=SUNKEN)
f1.pack(pady=20,fill=X)
Label(f1,text="WELCOME TO EXPENSE TRACKER", font="Helvetica 22 bold",fg="red").pack()

Button(root,text="Add Income",command=a_income,pady=10).pack()
Button(root,text="Add Expense",command=a_expense,pady=10).pack()
Button(root,text="Total Balance",command=check_balance,pady=10).pack()
Button(root,text="View Category Summary",command=cat_summary,pady=10).pack()
Button(root,text="Set Budget",command=budget,pady=10).pack()
Button(root,text="Budget Status",command=budget_stat,pady=10).pack()
Button(root,text="Quit",command=exit,pady=10).pack()
root.mainloop()