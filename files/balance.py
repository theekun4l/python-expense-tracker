from datetime import datetime

def balance(salary_dict,expenses_dict):
    date = datetime.now().strftime("%m-%y")
    Total_salary = 0.0
    Total_expenses = 0.0
    if date in salary_dict:
        for i in range(len(salary_dict[date])):
            Total_salary = Total_salary + salary_dict[date][i]['Income']
    if date in expenses_dict:
        for category in expenses_dict[date]:
            for i in range(len(expenses_dict[date][category])):
                Total_expenses = Total_expenses + expenses_dict[date][category][i]['Amount']

    return Total_expenses,Total_salary

def summary(expenses_dict):
    date = datetime.now().strftime("%m-%y")
    a = {}
    if date in expenses_dict:
        for category , items in expenses_dict[date].items():
            total = 0
            for item in items:
                total = total + item["Amount"]
            a[category] = total
    return a