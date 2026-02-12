#Building my own expense tracker!!
from datetime import datetime
import json
import os
from time import strftime
print("LOADING ALL NEEDED FILES!!")
expenses_dict = {}  
salary_dict = {}
budget_dict = {}  
if os.path.exists("salary.json"):
        with open("salary.json","r") as salary_loader:
            salary_dict = json.load(salary_loader)
else:
        with open("salary.json","w") as salary_loader:
            json.dump({},salary_loader)
if os.path.exists("expenses.json"):
        with open("expenses.json",'r') as expenses_loader:
            expenses_dict = json.load(expenses_loader)
else:
        with open("expenses.json",'w') as expenses_loader:
            json.dump({},expenses_loader)
if os.path.exists("budget.json"):
        with open("budget.json",'r') as budget_loader:
            budget_dict = json.load(budget_loader)
else:
        with open("budget.json",'w') as budget_loader:
            json.dump({},budget_loader)
while True:
    print("==================")
    print('''
1) Add income
2) Add Expense
3) View Balance
4) View Category Summary
5) Set Monthly Budget
6) Budget status
7) Exit 
''')
    try:
        user_input = int(input("Enter your choice (1-7): "))
    except ValueError:
         print("Invalid input!! Try again")
         continue
    print("==================")
    if user_input == 1:
       while True:
           try:
               sources = int(input("Number of sources of income: "))
           except ValueError:
               print("Invalid input!!  Try again")
               continue
           if sources <= 0:
               print("Number of sources cannot be 0/negative")
               continue
           else:
               break
       for i in range(sources):
            while True:
                try:
                    source_name = input("Source name:")
                    if source_name == '':
                        raise ValueError("source name cannot be empty")
                    elif source_name.isdigit():
                        raise ValueError("source name cannot be numeric")
                except ValueError as e:
                        print("Invalid input!! Try again.",e)
                        continue
                try:
                       user_salary = int(input("Enter Your income from given source: "))
                except ValueError:
                        print("Invalid input!!  Try again")
                        continue
                if user_salary <= 0:
                        print("Income cannot be 0/negative!! Try again")
                        continue
                else:
                        break
            date = datetime.now().strftime("%m-%y")
            date1 = datetime.now().strftime("%d-%m-%y")
            if date not in salary_dict:
                    salary_dict[date] = []
            salary_dict[date].append({
                        'Income': user_salary,
                        'Income Type': source_name,
                        'Date' : date1
                    })
       with open("salary.json",'w') as salary_updater:
            json.dump(salary_dict,salary_updater,indent=4)
       continue          
    elif user_input == 2:
        while True:
            try:
                Number_of_Expenses = int(input("Number of expenses: "))
            except ValueError:
                print("Invalid input")
                continue
            if Number_of_Expenses == 0:
                print("number of expenses cannot be 0")
                continue
            else:
                break
        for i in range(Number_of_Expenses):
            while True:
                try:
                    Expenses = int(input(f"Enter your expense {i+1} : "))
                except ValueError:
                    print("Invalid input!! Try again.")
                    continue
                if Expenses <=0:
                    print("Expenses cannot be negative/zero.")
                    continue
                try: 
                    Type = input("Type of expenses like food/gym/etc other stuff: ")
                    if Type == '':
                        raise ValueError("Type cannot be empty")
                    elif Type.isdigit():
                        raise ValueError("Type cannot be numeric")
                except ValueError as e:
                    print("Invalid input!! Try again.",e)
                    continue
                break
            date = datetime.now().strftime("%m-%y")
            if date not in expenses_dict:
                expenses_dict[date] = {Type : []} #iss line mai agar date exist nhi kart hogi toh uss date par ek dict assign kardega and dict mai current type kko empty list
            if Type not in expenses_dict[date]:
                expenses_dict[date][Type] = []  #iss line if date exist karti hai toh fir woh uss date mai key dhundega joki nhi hogi toh woh uss key ko list assign kardega
            date1 = datetime.now().strftime("%d-%m-%y")
            expenses_dict[date][Type].append({
                'Amount' : Expenses,
                'Category' : Type,                              #phele dict poori change karni then loop ke bad poori file save which is efficient way  
                'Date': date1})                            #dict change karna fast(memory stuff) and file save karna slow(disk stuff)
        with open("expenses.json",'w') as expenses_printer :
                json.dump(expenses_dict,expenses_printer,indent=4)
        continue
    elif user_input == 3:
        date = datetime.now().strftime("%m-%y")
        Total_salary = 0.0
        Total_expenses = 0.0
        if date in salary_dict:
            for i in range(len(salary_dict[date])):
                Total_salary = Total_salary + salary_dict[date][i]['Income']
            print(f"Total salary of month is: {Total_salary}")
        else:
             print("You haven\'t added salaary this month")
        if date in expenses_dict:
             for category in expenses_dict[date]:
                  for i in range(len(expenses_dict[date][category])):
                       Total_expenses = Total_expenses + expenses_dict[date][category][i]['Amount']
             print(f"Your total expenses are: {Total_expenses}")
        else:
             print("You haven't spend anything this month.")
        print(f"Net balance: {Total_salary - Total_expenses}")
        continue
    elif user_input == 4:
         date = datetime.now().strftime("%m-%y")
         if date in expenses_dict:
              for category in expenses_dict[date]:
                   category_total_expense = 0.0
                   for i in range(len(expenses_dict[date][category])):
                        category_total_expense = category_total_expense + expenses_dict[date][category][i]['Amount']
                   print(f"You spend on {category} is: {category_total_expense}")
         else:
              print("You haven\'t spend anything this month")  
         continue   
    elif user_input == 5:
        while True:
            try:
                user_budget = int(input("Set monthly budget: "))
            except ValueError:
                print("Invalid input!! Try again.")
                continue
            if user_budget <= 0:
                print("Budget cannot be negative/zero!! Try again")
                continue
            else:
                break
        date = datetime.now().strftime("%m-%y")
        budget_dict[date] = user_budget
        with open("budget.json",'w') as budget_updater:
             json.dump(budget_dict,budget_updater)
        continue
    elif user_input == 6:
        date = datetime.now().strftime("%m-%y")
        budget = 0.0
        Total_expenses = 0.0
        if date in budget_dict:
            budget = budget_dict[date] 
        if   budget == 0:
                print("First set budget!!!")
                continue
        if date in expenses_dict:
             for category in expenses_dict[date]:
                  for i in range(len(expenses_dict[date][category])):
                       Total_expenses = Total_expenses + expenses_dict[date][category][i]['Amount']
        remaining = budget - Total_expenses
        if budget > Total_expenses:
             print(f"You have remaining budget : {remaining}")
        elif budget < Total_expenses:
             print(f"WARNING : You have overspended your budget (budget - spend) = {budget - Total_expenses}")
        else:
             print("You have spent your all budget")
    elif user_input == 7:
         print("Thank you for tracking your finances responsibly,see you next month!")
         break
    else:
            print("Invalid input!! Try again")
            continue
             
         
    
                         