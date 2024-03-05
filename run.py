import datetime
import math


def get_vacation_year():
    """
    The user selects which vacation year they want to calculate.
    """
    while True:
        global vacation_year
        vacation_year = input(
            "Enter the vacation year you want to calculate (YYYY):\n")

        if validate_vacation_year(vacation_year):
            break

    global last_vac_year
    last_vac_year = int(vacation_year) - 1


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
        employment_date = input("Enter your employment date (YYYY-MM_DD):\n")

        if validate_employment_date(employment_date):
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
            "Enter the number of your holiday_entitlement (e.g. 25):\n")

        if validate_holiday_entitlement(holiday_entitlement):
            break


def validate_holiday_entitlement(holiday_entitlement):
    """
    Validates the holiday entitlement format and controls the minimum
    number of days (25).
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


def get_absence_data():
    """
    Get leave of absence data from the user.
    """
    while True:
        global absence_data
        absence_data = input(
            f"Enter the number of calender days with full leave of \
absence since {last_vac_year}-04-01:\n"
            )

        if validate_absence_data(absence_data):
            break


def validate_absence_data(absence_data):
    """
    Validate absence data format.
    """
    try:
        absence_data = int(absence_data)
    except ValueError:
        print("Incorrect absence data format, please try again.")
        return False

    return True


def calculate_employment_days(employment_date):
    """
    Calculate how many employment days the user got by comparing
    employment date and last day of vacation of the vacation year.
    """
    employment_date = datetime.datetime.strptime(employment_date, "%Y-%m-%d")

    vac_year = str(vacation_year)

    global last_day_vac_year
    last_day_vac_year = datetime.datetime.strptime(
        f"{vac_year}-04-01", "%Y-%m-%d")

    global last_day_last_vac_year
    last_day_last_vac_year = datetime.datetime.strptime(
        f"{last_vac_year}-04-01", "%Y-%m-%d")

    if employment_date <= datetime.datetime(int(last_vac_year), 4, 1):
        global emp_days
        emp_days = last_day_vac_year - last_day_last_vac_year
    else:
        emp_days = last_day_vac_year - employment_date


def calculate_paid_vacation_days(emp_days):
    """
    The calculation determines how many paid vacation days the user
    will receive by subtracting leave of absence days from total
    employment days.
    In the next step, the remaining days are related to the days in
    the current vacation year and multiplied by the vacation
    entitlement before being rounded up.
    """
    employ_days = int(emp_days.days)

    days_of_vac_year = last_day_vac_year - last_day_last_vac_year

    days_of_vac_year_int = int(days_of_vac_year.days)

    paid_vacation_days = (
        employ_days - int(absence_data))/days_of_vac_year_int *\
        int(holiday_entitlement)
    rounded_up_paid_vac_days = math.ceil(paid_vacation_days)
    print(f"You will get {rounded_up_paid_vac_days} paid vacation days \
{vacation_year}")


def main():
    """
    Run all program functions
    """
    get_vacation_year()
    get_employment_date()
    get_holiday_entitlement()
    get_absence_data()
    calculate_employment_days(employment_date)
    calculate_paid_vacation_days(emp_days)


print("Welcome to the Vacation Calculator!\n")
print("This is a calculator that computes how many paid vacation days \
you can expect to have this summer.\n")
print("It is based on your coverage under Swedish vacation law and \
considers the previous year as the accrual year.\n")

main()
