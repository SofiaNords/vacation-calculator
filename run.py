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
            "Enter the number of calender days with full leave of \
absence since -04-01:"
            )

        if validate_absence_data(absence_data):
            print(
                f"Your number of calender days with full leave of \
absence is: {absence_data}"
                )
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

    global last_vac_year
    last_vac_year = int(vacation_year) - 1

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
        print(f"Your employment days this year is {emp_days} days")
    else:
        print(f"Vacation year is {vacation_year}")
        print(f"Last day vacation year is {last_day_vac_year}")
        emp_days = last_day_vac_year - employment_date
        print(f"Your employment days this year is {emp_days} days")


def main():
    """
    Run all program functions
    """
    get_vacation_year()
    get_employment_date()
    get_holiday_entitlement()
    get_absence_data()
    calculate_employment_days(employment_date)


print("Welcome to the Vacation Calculator!\n")
print("This is a calculator that computes how many paid vacation days \
you can expect to have this summer.\n")
print("It is based on your coverage under Swedish vacation law and \
considers the previous year as the accrual year.\n")

main()
