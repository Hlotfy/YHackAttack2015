import urllib2
import operator
import json
import pprint

url = urllib2.Request("https://api.fiscalnote.com/committees?apikey=49BWNS84OZ0Y9CYZW4EJ7A7PVBFCY46N")

response = urllib2.urlopen(url)

response = response.read()

committees = json.loads(response)
print "list of legislators info: "
for group in committees: 
	#return committees.keys()
	print committees.keys()
	
