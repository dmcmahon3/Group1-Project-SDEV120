#This file contains modules that are called by main.py to view and modify the JSON database.

import json
employee_file = "employee_records.json"

def view_roster():
#This function lists all employee records with a break between each.
#An index number is assigned to each record based on its list position.
#The user will use this index number to select a record in other modules.
    print("\n\nEMPLOYEE RECORDS\n")
    with open (employee_file, "r") as f:
        employees = json.load(f)
        index_id = 1
        for entry in employees:
            employee_id = entry["employee_id"]
            employee_lastname = entry["employee_lastname"]
            employee_firstname = entry["employee_firstname"]
            employee_hourlyrate = entry["employee_hourlyrate"]
            employee_dependents = entry["employee_dependents"]
            employee_hoursworked = entry["employee_hoursworked"]
            print (f"Index Number: {index_id}")
            print (f"Employee ID:       {employee_id}")
            print (f"Last Name:         {employee_lastname}")
            print (f"First Name:        {employee_firstname}")
            print (f"Hourly Wage:       {employee_hourlyrate}")
            print (f"No. of Dependents: {employee_dependents}")
            print (f"Hours this period: {employee_hoursworked}")
            print ("\n")
            index_id = index_id + 1


def add_record():
# This function prompts the user to enter a new employee record.
# If an entry is invalid, the user is prompted to re-enter it.
# The new record is then appended to the end of the list.
# The file is overwritten with the updated list. It's then saved and closed.
    new_record = {}
    with open(employee_file, "r") as f:
        employees = json.load(f)
        #A list of employee ID's is generated for user entry to be checked against.
        current_id_list = []
        for item in employees:
            current_id_list.append(item["employee_id"])
        #Employee ID number must be unique, numeric, and a specific length.
        while True:
            new_record["employee_id"] = input("New Employee's ID (must be numeric, unique, and 6 digits): ")
            if len(new_record["employee_id"]) == 6\
                and new_record["employee_id"].isdigit() == True\
                    and new_record["employee_id"] not in current_id_list:
                break
            else:
                print("Employee ID too short, already in use, or contains non-numeric characters. Please re-enter.")                            
        #Last and first name entry must be alphabetic.
        while True:
            new_record["employee_lastname"] = input("New Employee's Last Name: ")
            if new_record["employee_lastname"].isalpha() == True:
                break
            else:
                print("Last name may only contain letters.")
        while True:
            new_record["employee_firstname"] = input("New Employee's First Name: ")
            if new_record["employee_firstname"].isalpha() == True:
                break
            else:
                print("First name may only contain letters.")
        #Hourly rate must be within a range.
        #Exception handling prevents crashing if user input isn't a float.
        while True:
            try:
                new_record["employee_hourlyrate"] = float(input("Employee's Hourly Rate: "))
                if new_record["employee_hourlyrate"] < 100 and new_record["employee_hourlyrate"] > 5:
                    break
                else:
                    print("Hourly rate entries must be between 5 and 100.")
            except:
                print("Hourly rate must be a number.")
        #Number of dependents. Input is converted from a string to an integer for calculations.
        while True:
            new_record["employee_dependents"] = input("Employee's No of Dependents: ")
            if new_record["employee_dependents"].isnumeric() == True\
                and int(new_record["employee_dependents"]) < 21:
                break
            else:
                print("Depedents entry must be a whole number and may not exceed 20.")
        new_record["employee_dependents"] = int(new_record["employee_dependents"])
        #Hours worked must be within a range.
        #Exception handling prevents crash if user input isn't a float.
        while True:
            try:
                new_record["employee_hoursworked"] = float(input("Hours Worked this period: "))
                if new_record["employee_hoursworked"] >= 1 and new_record["employee_hoursworked"] <= 168:
                    break
                else:
                    print("Hours worked may only be entered from 1-168.")
            except:
                print ("Hours worked entry must be a number.")
    #The new record is added to the list, which is rewritten to the JSON file.
        employees.append(new_record)
    with open (employee_file, "w") as f:
        json.dump(employees, f, indent=4)


def edit_record():
# This function prompts the user to select a record to edit by its index.
# Each unselected list item's data is overwritten with the original values.
# Once the selected record is reached, its values are overwritten by the user. 
# The list iteration resumes. When it completes, the file is saved and closed.
    view_roster()
    edited_record = []
    with open(employee_file, "r") as f:
        employees = json.load(f)
        roster_length = len(employees)
        # A list of employee ID's is generated for user entry to be checked against.
        current_id_list = []
        for item in employees:
            current_id_list.append(item["employee_id"])
        # The user is prompted to enter an index number of a record to edit.
        print ("Please select the index number of the record you wish to edit, or enter zero (0) to go back: ")
        while True:
            try:
                edit_selection = int(input(f"Select an index number from 1-{roster_length}: "))
                if edit_selection <= roster_length and edit_selection >= 0:
                    break
                else:
                    print(f"Selection must be from 1-{roster_length} or 0 to cancel.")
            except: 
                print ("Entry must be a number.")
        # The imported employee list is skipped over record by record, 
        # increasing a counter until the user's index selection is matched.
        # The program then identifies each field for use during the editing process.
        index_id=1
        for entry in employees:
            if index_id == int(edit_selection):
                employee_id = entry["employee_id"]
                employee_lastname = entry["employee_lastname"]
                employee_firstname = entry["employee_firstname"]
                employee_hourlyrate = entry["employee_hourlyrate"]
                employee_dependents = entry["employee_dependents"]
                employee_hoursworked = entry["employee_hoursworked"]
                # The program displays each field's current value to the user before prompting for input.
                print (f"Selected Index Number: {index_id}")
                # Employee ID must be unique, unless it is already in use.
                print (f"Employee's Current ID: {employee_id}")
                while True:
                    employee_id = input(
                        "Enter Employee's Updated ID (must be numeric, unique and 6 digits): ")
                    if len(employee_id) == 6\
                          and employee_id.isdigit() == True\
                            and employee_id not in current_id_list\
                                or employee_id == entry["employee_id"]:
                        break
                    else:
                        print("Employee ID too short, already in use, or contains non-numeric characters. Please re-enter.")                    
                # Last and first name must be alphabetic.
                print (f"Employee's Last Name: {employee_lastname}")
                while True:
                    employee_lastname = input("Enter Employee's Updated Last Name: ")
                    if employee_lastname.isalpha() == True:
                        break
                    else:
                        print("Last name may only contain letters.")
                print (f"Employee's First Name: {employee_firstname}")
                while True:
                    employee_firstname = input("Enter Employee's Updated First Name: ")
                    if employee_firstname.isalpha() == True:
                        break
                    else:
                        print("First name may only contain letters.")
                # Hourly rate must be within a range.
                # Exception handling prevents crashing if user input isn't a float.
                print (f"Employee's Current Hourly Wage: {employee_hourlyrate}")
                while True:                                   
                    try:
                        employee_hourlyrate = float(input("Enter Employee's Updated Hourly Rate: "))
                        if employee_hourlyrate < 100 and employee_hourlyrate > 5:
                            break
                        else:
                            print("Hourly rate entries must be between 5 and 100.")
                    except:
                        print("Hourly rate must be a number.")                                  
                # Number of dependents. Input is converted from a string to an integer for calculations.
                print (f"Employee's Reported No. of Dependents: {employee_dependents}")
                while True:
                    employee_dependents = input("Enter Employee's Updated No of Dependents: ")
                    if employee_dependents.isnumeric() == True and int(employee_dependents) < 21:
                        break
                    else:
                        print("Depedents entry must be a whole number and may not exceed 20.")
                employee_dependents = int(employee_dependents)
                print (f"Employee's Recorded Hours this period: {employee_hoursworked}")
                # Hours worked must be within an acceptable range.
                # Exception handling prevents crashing if user input isn't a float.
                while True:
                    try:
                        employee_hoursworked = float((input("Enter Employee's Updated Hours Worked this period: ")))
                        if employee_hoursworked >= 1 and employee_hoursworked <= 168:
                            break
                        else:
                            print("Hours worked may only be entered from 1-168.")
                    except:
                        print ("Hours worked entry must be a number.")
                #The updated information is added to the list in its current position.
                edited_record.append({
                    "employee_id": employee_id,
                    "employee_lastname": employee_lastname,
                    "employee_firstname": employee_firstname,
                    "employee_hourlyrate": employee_hourlyrate,
                    "employee_dependents": employee_dependents,
                    "employee_hoursworked": employee_hoursworked
                })
                index_id=index_id+1
            #Each record that is not updated is inserted back into its original list position
            #  with its current values.
            else:
                edited_record.append(entry)
                index_id=index_id+1
        with open (employee_file, "w") as f:
            json.dump(edited_record, f, indent=4)

def delete_record():
# This function prompts the user to delete an employee record from the list
# by selecting its index number. All records are overwritten with
# their original values except for the selected record, which is passed over.
# The file is saved and closed after the new list is written to it.
    view_roster()
    skipped_record = []
    with open(employee_file, "r") as f:
        employees = json.load(f)
        roster_length = len(employees)
    print ("Please select the index number of the record that you wish to erase, or enter zero (0) to cancel: ")
    while True:
            try:
                deletion_selection = int(input(f"Select an index number from 1-{roster_length}: "))
                if deletion_selection <= roster_length and deletion_selection >= 0:
                    break
                else:
                    print(f"Selection must be from 1-{roster_length} or 0 to cancel.")
            except: 
                print ("Entry must be a number.")
    index_id=1
    for entry in employees:
        if index_id == int(deletion_selection):
            pass
            index_id=index_id+1
        else:
            skipped_record.append(entry)
            index_id=index_id+1
    with open (employee_file, "w") as f:
        json.dump(skipped_record, f, indent=4)
