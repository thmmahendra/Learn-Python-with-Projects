# collect user preferences
# - length
# - should contain uppercase
# - should contain special
# - should contain digits

# get all available characters
# randomly pick characters up to the length
# ensure we have at least one of each character type
# ensure length is valid

import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be at least 4 character.")

generate_password()