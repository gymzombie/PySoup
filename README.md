# PySoup
This is a(n attempt at) python version of https://github.com/Jfaler/soup; an open
source call flooder using Twilio API.

It is a Telephony Denial of Service tool which is designed to repeatedly call telephone 
scammers to discourage them from calling people at home by keeping their phone lines busy. 

This type of attack is referred to as a TDoS or Telephony Denial of Service attack.
Please verify the legality of using this type of tool as it may be illegal in some areas. 

This tool is designed using Twilio for telephony connectivity. An account is required, and 
I would plan on spending $20 to $50 in funding this activity; more if you want to be 
exceptionally annoying. 


## Version
`
0.0.0.1a
`

This is pre-beta. At the moment I don't recommend running it, as I haven't even done a dry-run. 
You are welcome to fork and make changes, but don't run this unless you know some python and can help me catch errors. :-)

## Prerequisites

* Sign up with Twilio: https://www.twilio.com/try-twilio
* Make sure your system has python modules to support Twilio: `pip install twilio`

##Installation

`$ git clone https://github.com/gymzombie/PySoup`

## Usage
1. Copy settings.default to settings.local. 
2. Modify settings.local with your specific settings:
   - Twilio account details. 
   - Change the Payload if you don't like the provided sample. Use a TWIml formatted URL. 
   (My experience has been that Github is a poor hoster for this.)
   - Set your target number. These are the bad guys, though you may want to call yourself as a test. 
   - Set your "from" number(s). This can be retrieved from your Twilio console. 
3. Run `python3 pysoup.py` 

If you don't have Twilio numbers, I've created the `getnumber.py` script which will set them up for you and return your 
list. Just run `python3 getnumber.py 10` to setup 10 new numbers. This is not always necessary for an attack, but if you 
don't add some variety, they'll just block your number. 

## Caution
Note that nothing in these scripts "releases" (deletes) your Twilio phone numbers. You'll need to do that manually, 
or you will continue to be billed for their usage. 

## TODO

1. Get working
2. Test
3. Error checking
4. I was hoping it would integrate the "get number" script so it could spin up a new number, make some calls, 
then release that number.
