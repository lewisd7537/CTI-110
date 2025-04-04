# request employee information
name = input("Enter employee's name or \"Done\" to terminate: ")
# create accumulator variables for overtime pay, reg pay, gross pay, and one to count number of employees entered
overTime_total = 0.0
regPay_total = 0.0
gross_total = 0.0
Employee_count = 0
 
while name != "Done":
    # add one to Employee_count var
    Employee_count += 1
    # ask for employee information
    hoursWorked = float(input("How many hours did " + name + " work? "))
    payRate = float(input("What is " + name + "'s pay rate? "))
 
    # evaluate overtime
    if hoursWorked > 40:
        regular_hours = 40
        overtime_hours = hoursWorked - 40
        regular_pay = regular_hours * payRate
        overtime_pay = overtime_hours * (payRate * 1.5)
        gross_pay = regular_pay + overtime_pay
 
        # Accumulate totals
        overTime_total += overtime_pay
        regPay_total += regular_pay
    else:
        regular_pay = hoursWorked * payRate
        gross_pay = regular_pay
 
        # Accumulate totals
        regPay_total += regular_pay
 
    # Display output
    print("\nEmployee's name:  ", name, "\n")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('-' * 87)
    print(f'{hoursWorked:<15}{payRate:<12}{max(0, hoursWorked - 40):<12}{overtime_pay:<20}{regular_pay:<20}{gross_pay}')
    print()
 
    # ask user for another employee name
    name = input("Enter employee's name or \"Done\" to terminate: ")
 
# Display final results
# display overtime total, regular pay total, gross pay total, and number of employees entered
print("\nTotal number of employees entered: ", Employee_count, sep="")
print("Total amount paid for overtime: $", format(overTime_total, ".2f"), sep="")
print("Total amount paid for regular hours: $", format(regPay_total, ".2f"), sep="")
print("Total amount paid in gross: $", format(gross_total, ".2f"), sep="")