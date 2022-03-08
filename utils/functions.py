import names
from datetime import date


def generate_random_name(gender="male", first=True):
    """
    If first is True you will get a first name depending
     on which gender you've set in gender param
    :param gender: str
    :param first: bool
    :return: first or last name depending on arguments passed
    """
    return names.get_first_name(gender) if first else names.get_last_name()


def get_curr_date():
    return date.today().strftime("%d/%m/%Y")


#print(date.today().strftime("%d/%m/%Y  %hh/%mm/%hh"))