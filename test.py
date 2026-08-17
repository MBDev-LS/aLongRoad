
import json

testJsonDict = {
	'section_data': [{
		'sequential_id': '1631', # From which the uri can be derived
		'author_name': "Bob's little toe",
		'description': 'My carpet is a really cool shade of pink',
		'title': 'My carpet is cool'
	} for i in range (250)]
}

with open('test_for_loading.json', 'w') as jsonFile:
	jsonFile.write(json.dumps(testJsonDict))