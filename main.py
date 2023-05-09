import phonenumbers
from phonenumbers import carrier , geocoder , timezone

mobileNo = input("ENTER MOBILE NUMBER WITH COUNTRY CODE: ")
mobileNo = phonenumbers.parse(mobileNo)

#get timezone a phone number 
print(timezone.time_zones_for_number(mobileNo))

#getting a carrier for phonenumbers
print(carrier.name_for_number(mobileNo,"en"))

#getting region information
print(geocoder.description_for_number(mobileNo, "en"))

#validating a phonenumber
print("VALID MOBILE NUMBER: ", phonenumbers.is_valid_number(mobileNo))

#checking possibility of number
print("Checking possibility of number{}...", phonenumbers.is_possible_number(mobileNo))
# made by @GRINDis37 and edited by @Olittobee