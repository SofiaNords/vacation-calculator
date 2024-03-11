import datetime
import math
import pyfiglet
from colorama import Fore, Back


def get_vacation_year():
    """
    Prompts the user to input a vacation year (in YYYY format) and validates
    it.

    Returns:
        str: The validated vacation year.

    Example:
        >>> get_vacation_year()
        Enter the vacation year you want to calculate (YYYY): 2024
        '2024'
    """
    while True:
        global vacation_year
        vacation_year = input(Fore.RESET + "\nEnter the vacation year \
you want to calculate (YYYY): ").strip()

        if validate_vacation_year(vacation_year):
            break

    global last_vac_year
    last_vac_year = int(vacation_year) - 1


def validate_vacation_year(vacation_year):
    """
    Validates the format of a vacation year.

    Args:
        vacation_year (str): The year to validate (in the format YYYY).

    Returns:
        bool: True if the format is correct, otherwise False.

    Example:
        >>> validate_vacation_year("2024")
        True
        >>> validate_vacation_year("20XX")
        Incorrect vacation year format, please try again!
        False
    """
    try:
        vacation_year = datetime.datetime.strptime(vacation_year, "%Y")
    except ValueError:
        print(Fore.RED + "\nIncorrect vacation year format, please try again!")
        return False

    return True


def get_employment_date():
    """
    Prompts the user to input their employment date in the format (YYYY-MM-DD)
    and validates it.

    Returns:
        str: The validated employment date.

    Example:
        >>> get_employment_date()
        Enter your employment date (YYYY-MM-DD): 2022-03-15
        '2022-03-15'
    """
    while True:
        global employment_date
        employment_date = input(Fore.RESET + "\nEnter your employment date \
(YYYY-MM-DD): ").strip()

        if validate_employment_date(employment_date):
            break


def validate_employment_date(employment_date):
    """
    Validates the format of an employment date.

    Args:
        employment_date (str): The date to validate (in the format YYYY-MM-DD).

    Returns:
        bool: True if the format is correct, otherwise False.

    Example:
        >>> validate_employment_date("2022-03-15")
        True
        >>> validate_employment_date("20XX-01-01")
        Incorrect employment date format, please try again!
        False
    """
    try:
        employment_date = datetime.datetime.strptime(
            employment_date, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "\nIncorrect employment date format, \
please try again!")
        return False

    return True


def get_holiday_entitlement():
    """
    Prompts the user to input their holiday entitlement (number of
    vacation days) and validates it.

    Returns:
        str: The validated holiday entitlement (e.g., "25").

    Example:
        >>> get_holiday_entitlement()
        Enter the number of your holiday entitlement (e.g., 25): 20
        '20'
    """
    while True:
        global holiday_entitlement
        holiday_entitlement = input(Fore.RESET + "\nEnter the number \
of your holiday_entitlement (e.g. 25): ").strip()

        if validate_holiday_entitlement(holiday_entitlement):
            break


def validate_holiday_entitlement(holiday_entitlement):
    """
    Validates the format of holiday entitlement and ensures a minimum
    number of days (25).

    Args:
        holiday_entitlement (str): The number of vacation days to validate.

    Returns:
        bool: True if the format is correct and the number of days is at
        least 25, otherwise False.

    Example:
        >>> validate_holiday_entitlement("20")
        Incorrect holiday entitlement format, please try again!
        False
        >>> validate_holiday_entitlement("30")
        True
    """
    try:
        holiday_entitlement = int(holiday_entitlement)
        if holiday_entitlement < 25:
            print(Fore.RED + "\nHoliday entitlement must be at least \
25 days. Please try again!")
            return False
    except ValueError:
        print(Fore.RED + "\nIncorrect holiday entitlement format, \
please try again!")
        return False

    return True


def explain_absence_data():
    """
    Provides information about certain types of absence that qualify for
    vacation pay.

    Explanation:
        Certain types of absence should not be included in the total days
        of absence when calculating vacation entitlement.
        Here are the details:

        - Sick Leave: You can take up to 180 days of sick leave during
            the accrual year without affecting your paid vacation. This
            applies throughout the year of onset and the subsequent
            qualifying year.

        - Workplace Injury: If you experience a workplace injury, you’re
            eligible for absence during the year of onset and the following
            qualifying year.

        - Parental Leave: You can stay at home for a total of 120 days per
            child (or per pregnancy, regardless of whether it’s twins).

        - Care of a Sick Child: You’re entitled to 120 days of absence each
            qualifying year for caring for a sick child.

        - Pregnancy Allowance: During the authorized period, taking time
            off due to pregnancy doesn’t impact your paid vacation.

        - Disease Vector: If you’re carrying an infectious disease, you
            can be absent for up to 180 days during the qualifying year.

        - Dependent Care Support: You can take up to 45 days of absence
            during the qualifying year without affecting your vacation pay.

        - Certain Types of Education: Trade union training, sign language
            training for parents, and Swedish language teaching for
            immigrants do not impact your vacation pay during the first
            180 days.

    Example:
        >>> explain_absence_data()
        Before moving on, we recommend you to read about absence data.
        Do you want to read more about absence data? (y/n): y
        [Detailed explanation provided here...]
    """
    answer = input("\nBefore moving on, we recommend you to read about \
absence data. Do you want to read more about absence data? (y/n): ").strip()
    if answer.lower() == "y":
        print(Back.GREEN + "\nCertain types of absence qualify for \
vacation pay. These days should not be included in the total days \
of absence you will enter in the next step. Here are the details:\
\n\n - Sick Leave: You can take up to 180 days of sick leave during \
the accrual year without affecting your paid vacation. This applies \
throughout the year of onset and the subsequent qualifying year.\
\n\n - Workplace Injury: If you experience a workplace injury, you’re \
eligible for absence during the year of onset and the following \
qualifying year.\n\n - Parental Leave: You can stay at home for a \
total of 120 days per child (or per pregnancy, regardless of whether \
it’s twins). \n\n - Care of a Sick Child: You’re entitled to 120 days \
of absence each qualifying year for caring for a sick child.\
\n\n - Pregnancy allowance: During the authorized period, taking \
time off due to pregnancy doesn’t impact your paid vacation.\
\n\n - Disease Vector:  If you’re carrying an infectious disease, you \
can be absent for up to 180 days during the qualifying year.\
\n\n - Dependent Care Support: You can take up to 45 days of absence \
during the qualifying year without affecting your vacation pay.\
\n\n - Certain Types of Education: Trade union training, \
sign language training for parents, and Swedish language teaching \
for immigrants do not impact your vacation pay during the first \
180 days.\n")
    else:
        print(Fore.RESET + "\nOk, then you can move on without further \
explanation.")


def get_absence_data():
    """
    Prompts the user to input the number of calendar days with full leave
    of absence that doesn't include days qualified for vacation pay between
    {last_vac_year}-04-01 and {vacation_year}-03-31.

    Returns:
        str: The validated absence data (number of days).

    Example:
        >>> get_absence_data()
        Enter the number of calendar days with full leave of absence that
        doesn't include days qualified for vacation pay between 2023-04-01
        and 2024-03-31: 15
        '15'
    """
    while True:
        global absence_data
        absence_data = input(Fore.RESET + Back.RESET + f"\nEnter the number of \
calender days with full leave of absence that doesn't include \
days qualified for vacation pay between {last_vac_year}-04-01 \
and {vacation_year}-03-31: ").strip()

        if validate_absence_data(absence_data):
            break


def validate_absence_data(absence_data):
    """
    Validates the format of absence data.

    Args:
        absence_data (str): The number of days with full leave of
            absence that doesn't include days qualified for vacation
            pay between {last_vac_year}-04-01 and {vacation_year}-03-31.

    Returns:
        bool: True if the format is correct, otherwise False.

    Example:
        >>> validate_absence_data("15")
        True
        >>> validate_absence_data("abc")
        Incorrect absence data format, please try again!
        False
    """
    try:
        absence_data = int(absence_data)
    except ValueError:
        print(Fore.RED + "\nIncorrect absence data format, please try again!")
        return False

    return True


def calculate_employment_days(employment_date):
    """
    Calculates the number of employment days based on the provided
    employment date.

    Args:
        employment_date (str): The employment start date in the
        format (YYYY-MM-DD).

    Explanation:
        The function calculates the employment days between
        {last_vac_year}-04-01 and {vacation_year}-03-31. If the
        employment date is before or on {last_vac_year}-04-01, it
        considers the entire period from {last_vac_year}-04-01 to
        {vacation_year}-03-31. Otherwise, it calculates the days
        from the employment date to {vacation_year}-03-31.

    Returns:
        datetime.timedelta: The duration of employment in days.

    Example:
        >>> calculate_employment_days("2023-01-15")
        datetime.timedelta(days=366)
        >>> calculate_employment_days("2023-05-10")
        datetime.timedelta(days=327)
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
    Calculates the number of paid vacation days based on employment days
    and absence data.

    Args:
        emp_days (datetime.timedelta): The duration of employment in days.

    Returns:
        None: Prints the calculated paid vacation days and, if applicable,
        unpaid vacation days.

    Explanation:
        The function calculates the paid vacation days for the period between
        {last_vac_year}-04-01 and {vacation_year}-03-31. It considers the
        employment duration, absence data, and holiday entitlement.

    Example:
        >>> calculate_paid_vacation_days(datetime.timedelta(days=292))
        You will get 20 paid vacation days in 2024!
        You will also receive 5 unpaid vacation days as you are entitled to
        25 vacation days each year.
    """
    employ_days = int(emp_days.days)

    days_of_vac_year = last_day_vac_year - last_day_last_vac_year

    days_of_vac_year_int = int(days_of_vac_year.days)

    paid_vacation_days = (
        employ_days - int(absence_data))/days_of_vac_year_int *\
        int(holiday_entitlement)

    rounded_up_paid_vac_days = math.ceil(paid_vacation_days)
    print(Back.MAGENTA + f"\nYou will get {rounded_up_paid_vac_days} \
paid vacation days {vacation_year}!")

    if rounded_up_paid_vac_days < int(holiday_entitlement):
        unpaid_vacation_days = int(
            holiday_entitlement) - rounded_up_paid_vac_days
        print(f"\nYou will also receive {unpaid_vacation_days} unpaid \
vacation days as you are entitled to {holiday_entitlement} vacation days \
each year.")


def main():
    """
    Executes all program functions in the specified order.

    Explanation:
        This function orchestrates the entire process of collecting input
        data, explaining absence details, calculating employment days, and
        determining paid vacation days.

    Example:
        >>> main()
        [Program execution details...]
    """
    get_vacation_year()
    get_employment_date()
    get_holiday_entitlement()
    explain_absence_data()
    get_absence_data()
    calculate_employment_days(employment_date)
    calculate_paid_vacation_days(emp_days)


if __name__ == "__main__":
    result = pyfiglet.figlet_format("Vacation Calculator")
    print(result)
    print("This calculator works out how many paid vacation days you \
can expect in a vacation year.\n")
    print("The calculator is adapted to the Swedish vacation law \
and assumes that the previous year is the qualifying year.")
    main()
