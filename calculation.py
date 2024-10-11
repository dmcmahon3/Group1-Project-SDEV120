import json

json_data = open("employee_records.json")


result = json.load(json_data)

id_list = []
for item in result:
    id_list.append(item["employee_id"])

selected_id = (
     input("Enter an employee ID number from above to calculate pay:\n"))
while selected_id not in id_list:
     print("Selected ID not found.")
     selected_id = input("Enter an employee ID number from above to calculate pay:")
   
for item in result:
    if selected_id == item["employee_id"]:
        last_name = item["employee_lastname"]
        first_name = item["employee_firstname"]
        employee_hourlyrate = item["employee_hourlyrate"]
        employee_dependents = item["employee_dependents"]
        hours_worked = item["employee_hoursworked"]

# calculate_gross_pay
def calculate_gross_pay(hours_worked, employee_hourlyrate):
    over_time_hours = 0
    over_time_hours = employee_hourlyrate * 1.5
    if hours_worked > 40:
            calculate_gross_pay = (40 * employee_hourlyrate) + (over_time_hours * (hours_worked - 40))
    else:
            calculate_gross_pay = hours_worked * employee_hourlyrate
    return calculate_gross_pay


gross_pay = round(calculate_gross_pay(hours_worked, employee_hourlyrate), 2)


# pre-tax amount
def calc_pre_tax_amount(gross_pay, employee_dependents):
    global dependents_deduction
    dependents_deduction = employee_dependents * 25
    pre_taxes = gross_pay - dependents_deduction


    return pre_taxes

pre_tax_amount = calc_pre_tax_amount(gross_pay, employee_dependents)

# post tax amount
def calc_net_pay(pre_tax_amount):
    global state_tax
    global federal_tax
    state_tax = round((pre_tax_amount * 0.056), 2)
    federal_tax = round((pre_tax_amount * 0.079), 2)
    netpay_amount = pre_tax_amount - state_tax - federal_tax
    return netpay_amount

netpay = round(calc_net_pay(pre_tax_amount), 2)

def print_employee_info():
# Prints employee paystub info and rounds it to two decimal places.
    print(f"Employee Name: {first_name} {last_name}")
    if hours_worked > 40:
        print(f"Hours Worked: {hours_worked} ({round((hours_worked - 40), 2):} overtime)")
    else:
        print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: ${employee_hourlyrate:}")
    print(f"Gross Pay: ${gross_pay}")
    if employee_dependents > 0:
        print(f"Pre-Tax Deductions: ${dependents_deduction} ({employee_dependents} dependents at $25 each)")
    else:
         print(f"Pre-Tax Deductions: ${dependents_deduction} (No dependents)")
    print(f"Federal Tax Witheld: ${federal_tax}")
    print(f"State Tax Withheld: ${state_tax}")
    print(f"Net Pay: ${netpay}")
    print("\n---\n")

print_employee_info()
