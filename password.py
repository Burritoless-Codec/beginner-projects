import random
import string


def gen_pass(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if numbers:
        chars += digits
    if special_chars:
        chars += special

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(chars)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
    return pwd


min_length = int(input('Enter length: '))
has_num = input('Password has numbers (Y/n)? ').lower() == "y"
has_spec = input('Password has special characters (Y/n)? ').lower() == "y"

pwd = gen_pass(min_length, has_num, has_spec)
print(f'Password generated: {pwd}')
