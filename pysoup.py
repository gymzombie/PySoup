#!/usr/bin/env python3

from twilio.rest import Client
# reference: https://github.com/twilio/twilio-python/

# Import configuration settings
execfile("./settings.default")
execfile("./settings.local")

# Python3 version:
# exec(open("./settings.local").read())

# TODO: Check initialization:
#  * Not using default twilio account
#  * a target has been provided
#      * Regex to verify correct format?
#      * Optional: If one has not been provided in the settings, ask the user for input?
#      * Optional: If any of the settings are set to defaults, kick the user out with instructions
#  * We have a message to send



def makecalls():

        # Use the target provided in the settings file, else ask the user to provide one:
            # Ask the user for a phone number to target:
        # target = input('Enter the target number to start flood (+1 MUST BE IN FRONT!):')

        fromnumber = 8047290441
        new_call = Client.calls.create(to=targetnum, from_=fromnumber, url=twilioXMLPayload)

        print('Started call to :" + targetnum + " from: " + FromNumber')
        # TODO: Catch errors from bad numbers here



if __name__ == '__main__':
    makecalls()
