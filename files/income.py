from .storage import save_file
from datetime import datetime
def add_income(salary_dict,user_salary,source_name):
     date = datetime.now().strftime("%m-%y")
     date1 = datetime.now().strftime("%d-%m-%y")
     if date not in salary_dict:
         salary_dict[date] = []
         salary_dict[date].append({
         'Income': user_salary,
         'Income Type': source_name,
         'Date': date1
     })
     else:
         salary_dict[date].append({'Income': user_salary,
         'Income Type': source_name,
         'Date': date1})
     save_file("salary.json",salary_dict)
     return salary_dict