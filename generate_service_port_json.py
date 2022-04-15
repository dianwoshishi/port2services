from collections import defaultdict
import re
import json
import requests

import yaml

# url = "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv"

service_names_port_number = "service-names-port-numbers.csv"
port_match =  r'(\d{0,}\-?\d+.*?)'

port_description = defaultdict(list)
# ["Service_Name","Port_Number","Transport_Protocol","Description","Assignee","Contact","Registration_Date","Modification_Date","Reference","Service_Code","Unauthorized_Use_Reported","Assignment_Notes" ])
with open(service_names_port_number, "r") as f:
	for i, line in enumerate(f):
		line = line.strip()
		if i == 0:
			continue
		else:
			line = line.split(",")
			if len(line) < 2:
				# print(line)
				continue

			port = line[1]
			matchObj =  re.match(port_match, port, re.M|re.I)
			if matchObj:
				# print("matchObj.group() : ", matchObj.group())
				port = matchObj.group()
				if '-' in port:
					try:
						port_range = port.split('-')
						for i in range(int(port_range[0]), int(port_range[1])+1):
							# print(f'{i}, {line[2]}-{line[0]}-{line[3]}')
							port_description[str(i)].append(f"{line[2]}-{line[0]}-{line[3]}")
					except Exception as e:
						# print(line, e)
						continue
				else:
					try:
						# print(f'{line[1]}, {line[2]}-{line[0]}-{line[3]}')
						port_description[str(line[1])].append(f"{line[2]}-{line[0]}-{line[3]}")
					except Exception as e:
						# print(line, e)
						continue

def write_json(port_description):
	json_port_description = json.dumps(port_description)
	print(json_port_description)

write_json(port_description)


def write_yaml(port_description, outputfile):
	with open(outputfile, 'w') as file:
		yaml.dump(port_description, file)

write_yaml(port_description, "service-names-port-numbers.csv.yml")