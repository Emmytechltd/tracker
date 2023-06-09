import phonenumbers
from phonenumbers import geocoder, carrier, timezone
number = input("Enter your number: ")
phone_number = phonenumbers.parse(number)
print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")
print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
print(f"Time_Zone: {timezone.time_zones_for_geographical_number(phone_number)}")