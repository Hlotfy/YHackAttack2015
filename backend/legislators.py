import urllib2
import operator
import json
import pprint

url = urllib2.Request("https://api.fiscalnote.com/legislators?apikey=49BWNS84OZ0Y9CYZW4EJ7A7PVBFCY46N")
#print "Before request"
response = urllib2.urlopen(url)
#print "After urlopen"
response = response.read()
#print "after read response"
legislators = json.loads(response)
print "list of legislators info: "
for rep in legislators: 
	print "state: "
	print rep['state']
	print "name: "
	print rep['first_name'], rep['last_name']
	
