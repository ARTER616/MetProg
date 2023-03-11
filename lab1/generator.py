import random
import string

def generate_work_phone():
    """! Generates a 11-digit work phone number that starts with '7'.

    @return: 11-digit work phone number as a string
    """
    return "7" + "".join([str(random.randint(0, 9)) for i in range(10)])

def generate_full_name():
    """! Generates a random full name.

    @return: Full name as a string
    """
    first_name = "".join(random.choice(string.ascii_letters) for i in range(random.randint(3, 10)))
    last_name = "".join(random.choice(string.ascii_letters) for i in range(random.randint(3, 10)))
    return f"{first_name.capitalize()} {last_name.capitalize()}"

def generate_email(name):
    """! Generates an email address based on the name, with a random domain and number.

    @param name: Full name of the person
    @return: Email address as a string
    """
    name = name.split(" ")
    number = str(random.randint(1940, 2017))
    domain = "".join(random.choice(string.ascii_letters) for i in range(random.randint(3, 7)))
    return f"{name[0].lower()}.{name[1].lower()}{number}@{domain.lower()}.com"

def generate_org_name():
    """! Generates a random 10-character organization name with uppercase letters.

    @return: Organization name as a string
    """
    return "".join(random.choice(string.ascii_letters) for i in range(10)).upper()
    