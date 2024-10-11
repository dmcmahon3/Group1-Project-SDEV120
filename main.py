import sys
import inputs

print("WEEKLY PAYROLL CALCULATOR\n(by Group 1)")
#This function presents a list of options for users.
def display_menu():
    print("\nOPTIONS:")
    print("(1) View Employee Roster")
    print("(2) Add Employee Record")
    print("(3) Edit Employee Record")
    print("(4) Delete Employee Record")
    print("(5) Calculate Pay")
    print("(6) Exit")
#A loop that prompts the user to select an option, then calls its function. 
while True:
    display_menu()
    menu_choice = input("\nSelect an option from 1-6: ")
    if menu_choice == "1":
        inputs.view_roster()
    elif menu_choice == "2":
        inputs.add_record()  
    elif menu_choice == "3":
        inputs.edit_record()
    elif menu_choice == "4":
        inputs.delete_record()
    elif menu_choice == "5":
        inputs.view_roster()
        with open("calculation.py") as calculations:
            exec(calculations.read())   
    elif menu_choice == "6":
        sys.exit()          
    else:
        print ("\nInvalid selection.")

