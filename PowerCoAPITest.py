__author__ = 'jpdixon'

# import statements
from sys import argv
import urllib2
import urllib
import time
import sys

# method definitions

# get the number of records in the file
def getNumberOfRecords(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# class definitions

## Main
script, args0 = argv

# take the fileName as the first argument, and the endpoint URL as the second argument
baseurl=args0

print "GETCity v1.0"

for i in range(1,100000):
    url=baseurl + "/" + str(i)
    startTime=int(round(time.time() * 1000))
    endTime=0;
    sys.stdout.write(url + ": GETting city " + str(i) + "... ")

    opener=urllib2.build_opener()

    opener.addheaders=[('Accept', 'application/json')]

    try:
        response = opener.open(url).read()

        endTime=int(round(time.time() * 1000))
        print "done (" + str(endTime-startTime) + " ms)."

        print str(response)


    except urllib2.HTTPError:
        print "Error in GET..."
        i=i-1
        continue

    # we can sleep for 2 seconds so we don't overwhelm the server from one URL
    #time.sleep(2)
# end for loop


