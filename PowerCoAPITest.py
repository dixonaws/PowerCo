__author__ = 'dixonaws@amazon.com'

# import statements
from sys import argv
import urllib2
import urllib
import time
import sys
import json

## Main
script, args0 = argv

# take the fileName as the first argument, and the endpoint URL as the second argument
baseurl=args0

print "PowerCo API Test, v1.0"

url=baseurl
startTime=int(round(time.time() * 1000))
endTime=0;
sys.stdout.write(url + ": GETting invoice... ")

opener=urllib2.build_opener()

# ask the API to return JSON
opener.addheaders=[('Accept', 'application/json')]

try:
    # our response string should result in a JSON object
    response = opener.open(url).read()

    endTime=int(round(time.time() * 1000))
    print "done (" + str(endTime-startTime) + " ms)."

    print str(response)


except urllib2.HTTPError:
    print "Error in GET..."

# decode the returned JSON response into JSONInvoice (a Python dict object)
JSONinvoice = json.loads(str(response))


print JSONinvoice
strAmountDollars=str(JSONinvoice['amountDollars'])
strAmountCents=str(JSONinvoice['amountCents'])

print "The amount of the invoice object returned is: " + strAmountDollars



