from datetime import datetime
from .storage import save_file
def add_expense(expenses_dict,expense,source_name):
        date = datetime.now().strftime("%m-%y")
        if date not in expenses_dict:
            expenses_dict[date] = {
                source_name: []}
        else:
            if source_name not in expenses_dict[date]:
                expenses_dict[date][source_name] = []
                date1 = datetime.now().strftime("%d-%m-%y")
                expenses_dict[date][source_name].append({
                'Amount': expense,
                'Category': source_name,
                'Date': date1})
            else:
                date1 = datetime.now().strftime("%d-%m-%y")
                expenses_dict[date][source_name].append({ 'Amount': expense,
                'Category': source_name,
                'Date': date1})
        save_file("expenses.json",expenses_dict)
        return expenses_dict

