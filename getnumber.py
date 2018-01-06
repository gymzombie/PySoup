# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account. By default we're just inhereting them from
# your settings.local file

exec(open("./settings.local").read())

client = Client(accountSid, authtoken)

numbers = client.available_phone_numbers("US") \
                .local \
                .list()

# Retrieve a new random phone number (Note this costs $1/month per number):
number = client.incoming_phone_numbers \
               .create(phone_number=numbers[0].phone_number)

# Retrieve a list of your phone numbers:
for number in client.incoming_phone_numbers.list():
    print('Deleting ' + number.phone_number)
    client.

