#!/bin/python



from twilio.rest import Client

# reference: https://github.com/twilio/twilio-python/


account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)


def example():

    target = input('Enter the target number to start flood (+1 MUST BE IN FRONT!):')
    new_call = client.calls.create(to='XXXX', from_='YYYY', method='GET')


if __name__ == '__main__':
    makecalls()
