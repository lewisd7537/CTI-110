#Your Name
#Date
#Assignment Name
#Brief description of program

import random

def disperse_change(change_owed):
    """
    This function takes the amount of change owed to the customer and
    calculates the number of dollars, quarters, dimes, nickels, and pennies
    required to make the change.
    """
    dollars = int(change_owed // 1)
    change_owed -= dollars
    quarters = int(change_owed // 0.25)
    change_owed -= quarters * 0.25
    dimes = int(change_owed // 0.10)
    change_owed -= dimes * 0.10
    nickels = int(change_owed // 0.05)
    change_owed -= nickels * 0.05
    pennies = int(round(change_owed * 100))

    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


def main():


    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed}")

    cash_put_in = float(input("How much cash will you put in the self-checkout? "))

    change_owed = cash_put_in - total_owed
    print(f"Change is: ${change_owed:.2f}")

    disperse_change(change_owed)


if __name__ == "__main__":
    main()