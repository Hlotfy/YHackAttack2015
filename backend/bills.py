import urllib2
import operator
import json
import pprint

url = urllib2.Request("https://api.fiscalnote.com/bills?apikey=49BWNS84OZ0Y9CYZW4EJ7A7PVBFCY46N")

response = urllib2.urlopen(url)

response = response.read()

bills = json.loads(response)
print "list of bill info: "
for bill in bills: 
	#return bill.keys()
	print bill.keys()
	
