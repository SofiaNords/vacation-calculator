import datetime


def get_vacation_year():
    """
    The user selects which vacation year they want to calculate
    """
    while True:
        global vacation_year
        vacation_year =
        input("Enter the vacation year you want to calculate (YYYY):")

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


def main():
    """
    Run all program functions
    """
    get_vacation_year()


main()
