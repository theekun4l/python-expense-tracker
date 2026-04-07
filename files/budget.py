from datetime import datetime
from .storage import save_file

def set_budget(budget_dict,user_budget):

    date = datetime.now().strftime("%m-%y")
    budget_dict[date] = user_budget
    save_file("budget.json",budget_dict)

def budget_status(budget_dict,expenses_dict):
    date = datetime.now().strftime("%m-%y")
    budget = 0.0
    Total_expenses = 0.0
    if date in budget_dict:
        budget = budget_dict[date]
    else:
        return
    if budget == 0:
        return False
    if date in expenses_dict:
        for category in expenses_dict[date]:
            for i in range(len(expenses_dict[date][category])):
                Total_expenses = Total_expenses + expenses_dict[date][category][i]['Amount']
    remaining = budget - Total_expenses
    return budget, Total_expenses, remaining