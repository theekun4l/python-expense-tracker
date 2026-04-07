import json
import os

def load_file(file_name):

   if os.path.exists(file_name):
        with open(file_name,"r") as file_loader:
           try:
                return json.load(file_loader)
           except :
               return
   else:
        with open(file_name,"w") as file_maker:
            json.dump({},file_maker)
            return {}

def save_file(file_name,data):
    with open(file_name,"w") as file_saver:
        json.dump(data,file_saver,indent=4)
