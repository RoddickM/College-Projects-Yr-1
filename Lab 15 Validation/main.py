from validation import *
import pandas as pd

data_validated = {
    "First Name": [],
    "Last Name": [],
    "Email Address": [],
    "Street": [],
    "District": [],
    "Town": [],
    "County": [],
    "Post Code": [],
    "Date of Birth": [],
    "Age": [],
}

first_name = length_validation(text="Please enter your name: ", length_needed=30)

last_name = length_validation(text="Please enter your last name: ", length_needed=20)

email_address = has_character(text="Please enter your email address: ", has="@")

address_street = length_validation(text="Please enter the name of your street: ", length_needed=20)

address_district = length_validation(text="Please enter the name of your district: ", length_needed=20)

address_town = length_validation(text="Please enter the name of your town/city: ", length_needed=20)

address_county = length_validation(text="Please enter the name of your county: ", length_needed=20)

post_code = post_code_validation(text="Please enter your postcode: ")

date_of_birth = date_validation(text="Please enter your date of birth(use DD/MM/YYYY format): ")

age_of_user = age_validation(text="Please enter your age: ", age_start=18, age_end=76)

output = f"\nYour first name is: {first_name.title()}"
output += f"\nYour last name is: {last_name.title()}"
output += f"\nYour email address is: {email_address}"
output += f"\nYour street name is: {address_street.title()}"
output += f"\nYour district is: {address_district.title()}"
output += f"\nYour town name is: {address_town.title()}"
output += f"\nYour county name is: {address_county.title()}"
output += f"\nYour postcode is: {post_code}"
output += f"\nYour  date of birth is: {date_of_birth}"
output += f"\nYour age name is: {age_of_user}"

print(output)

data_validated["First Name"].append(first_name.title())
data_validated["Last Name"].append(last_name.title())
data_validated["Email Address"].append(email_address)
data_validated["Street"].append(address_street.title())
data_validated["District"].append(address_district.title())
data_validated["Town"].append(address_town.title())
data_validated["County"].append(address_county.title())
data_validated["Post Code"].append(post_code.title())
data_validated["Date of Birth"].append(date_of_birth)
data_validated["Age"].append(age_of_user)

data_frame = pd.DataFrame(data_validated)
