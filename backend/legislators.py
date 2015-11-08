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
	
# get user's input
user_input = str(input("What state do you live in"))
list_of_legistrators = []
for rep in legislators:
	if rep['state'] == user_input:
		list_of_legistlators.append(rep)
	return list_of_legistlators
		
