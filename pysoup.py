#!/usr/bin/env python3

# See Readme.md for details and instructions

from twilio.rest import Client
# reference: https://github.com/twilio/twilio-python/

# Import configuration settings
exec(open("./settings.default").read())
exec(open("./settings.local").read())


def verify():
    if accountSid == "ACXXXXXXXXXXXXXXXXX"
        print("Your settings.local file has not been created, or has not been modified to reflect your account SID.")
        exit()
    if authtoken == "YYYYYYYYYYYYYYYYYY"
        print("Your settings.local file has not been created, or has not been modified to reflect your authtoken.")
        exit()
    if targetnum == "+15555551234"
        print('Please update your settings.local file with a correct target number')
        exit()
    if targetnum != \+1[2-9](\d{1,9})
        print('Please update your settings.local file with a target number formatted as +12024561212')
        exit()


def makecall():

    client = Client(accountSid, authtoken)
    new_call = client.calls.create(to=targetnum, from_=fromnumber, url=twilioXMLPayload)
    print('Started call to :' + targetnum + ' from: ' + fromnumber)
    # TODO: Catch errors from bad numbers here





# TODO: Separate function for looping the calls



verify()

if __name__ == '__main__':
    makecall()

