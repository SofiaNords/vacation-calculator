import datetime


def get_vacation_year():
    """
    The user selects which vacation year they want to calculate.
    """
    while True:
        global vacation_year
        vacation_year = input(
            "Enter the vacation year you want to calculate (YYYY):")

        if validate_vacation_year(vacation_year):
            print(f"Thank you, your vacation year is {vacation_year}.")
            break


def validate_vacation_year(vacation_year):
    """
    Validates vacation year date format.
    """
    try:
        vacation_year = datetime.datetime.strptime(vacation_year, "%Y")
    except ValueError:
        print("Incrorrect employment date format, please try again.")
        return False

    return True


def get_employment_date():
    """
    Get employment date from the user.
    """
    while True:
        global employment_date
        employment_date = input("Enter your employment date (YYYY-MM_DD):")

        if validate_employment_date(employment_date):
            print(f"Thank you, your employment date is {employment_date}.")
            break


def validate_employment_date(employment_date):
    """
    Validate employment date format.
    """
    try:
        employment_date = datetime.datetime.strptime(
            employment_date, "%Y-%m-%d")
    except ValueError:
        print("Incorrect employment date format, please try again!")
        return False

    return True


def get_holiday_entitlement():
    """
    Get holiday entitlement from the user.
    """
    while True:
        global holiday_entitlement
        holiday_entitlement = input(
            "Enter the number of your holiday_entitlement (e.g. 25):")

        if validate_holiday_entitlement(holiday_entitlement):
            print(f"Your holiday entitlement is: {holiday_entitlement}")
            break


def validate_holiday_entitlement(holiday_entitlement):
    """
    Validates the holiday entitlement format and controls the minimum number of days (25).
    """
    try:
        holiday_entitlement = int(holiday_entitlement)
        if holiday_entitlement < 25:
            print("Holiday entitlement must be at least 25 days.")
            return False
    except ValueError:
        print("Incorrect holiday entitlement format, please try again.")
        return False

    return True


def main():
    """
    Run all program functions
    """
    get_vacation_year()
    get_employment_date()
    get_holiday_entitlement()


print("Welcome to the Vacation Calculator!\n")
print("This is a calculator that computes how many paid vacation days \
you can expect to have this summer.\n")
print("It is based on your coverage under Swedish vacation law and \
considers the previous year as the accrual year.\n")

main()
