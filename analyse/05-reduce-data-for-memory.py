#!/usr/bin/env python3
import json
import re

memoryfilename = '03-result-memory.json'
outputfilename = '06-result-memory.json'

inputfile = open(memoryfilename)
memorydata = json.load(inputfile)
inputfile.close()
print('Eingabeatei {0} enthält {1} Einträge.'.format(memoryfilename, len(memorydata)))

results = []

for record in memorydata:
	'''ID aus Bild-URI extrahieren'''
	recordId = recordId = re.findall(r'record_(.*)_media.*', record['back'])[0]

	results.append({
        'id': recordId,
        'uri': record['uri'],
        'title': record['title'],
        'year': record['date'],
        'owner': record['owner']
    })


print('Schreibe {0} Einträge in {1}'.format(len(results), outputfilename))

with open(outputfilename, 'w') as f:
	json.dump(results, f, sort_keys=True, indent=4, separators=(',', ': '))
