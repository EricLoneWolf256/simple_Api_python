import phonenumbers
from phonenumbers import geocoder, carrier

# Parse the phone numbers
phone_number1 = phonenumbers.parse("+256760226156")
phone_number2 = phonenumbers.parse("+254739217438")

print("\nPhone Number Information\n")

# Location (Country/Region)
print("Location 1:", geocoder.description_for_number(phone_number1, "en"))
print("Location 2:", geocoder.description_for_number(phone_number2, "en"))

# Carrier (MTN, Airtel, etc.)
print("Carrier 1:", carrier.name_for_number(phone_number1, "en"))
print("Carrier 2:", carrier.name_for_number(phone_number2, "en"))

for i in range (1,13):
    for j in range(1,13):
        print(i*j, end="\t")
    print()