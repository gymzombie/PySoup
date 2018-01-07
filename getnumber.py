# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import sys

# We're just inheriting your Twilio account details from your settings.local file

exec(open("./settings.local").read())

print('Preparing to create ' + sys.argv[1] ' new Twilo numbers at $1/month per number. '
input('Press Enter now to continue, or Control + C to exit')

client = Client(accountSid, authtoken)

# Retrieve a new phone number (Note this costs $1/month per number):
numbers = client.available_phone_numbers("US") \
                .local \
                .list()

number = client.incoming_phone_numbers \
               .create(phone_number=numbers[0].phone_number)

# Retrieve a complete list of your phone numbers:
for allnumbers in client.incoming_phone_numbers.list():
    print('All numbers registered to your account:')
    print(allnumbers.phone_number)

