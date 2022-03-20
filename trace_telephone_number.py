import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import functools
import operator

number = input("Please, a telephone number, that you want to track: ")
ch_number = phonenumbers.parse(number, "CH")
print("Country: " + geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "RO")
print("Service provider: " + carrier.name_for_number(service_number, "en"))

target_timezone_source = timezone.time_zones_for_number(ch_number)
target_timezone = functools.reduce(operator.add, (target_timezone_source))
print("Timezone: " + target_timezone)
