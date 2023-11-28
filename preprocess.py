import csv
import os

headers=['DAY_OF_WEEK', 'FL_DATE', 'OP_UNIQUE_CARRIER', 'ORIGIN_AIRPORT_ID', 'ORIGIN', 'DEST_AIRPORT_ID', 'DEST', 'DEP_DELAY', 'DEP_DEL15', 
'ARR_DELAY', 'ARR_DEL15', 'ACTUAL_ELAPSED_TIME', 'AIR_TIME', 'DISTANCE', 'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']


key_headers=["ARR_DEL15","DEP_DEL15","CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY", "ORIGIN", "DEST", "OP_UNIQUE_CARRIER"]

dataset=[]

def checkNot(d, k, v, parseFunc=str): return d[k].strip() and parseFunc(d[k].strip()) != v

def checkNotGroup(d,keys, v, parseFunc=str): return sum([ 1 if checkNot(d,key, v, parseFunc) else 0 for key in keys]) >= 1

def check(d, k, v, parseFunc=str): return d[k].strip() and parseFunc(d[k].strip()) == v

def checkGroup(d,keys, v, parseFunc=str): return sum([ 1 if check(d,key, v, parseFunc) else 0 for key in keys]) >= 1

airlines_to_filter=dict()
origins_to_filter=dict()
dest_to_filter=dict()


def addMap(map, key):
	if key not in map.keys():
		map[key] = 1
	else:
		map[key] += 1

### Combine and select raw data

def preprocess():
	print(f"Pre process running !!")

	complete_data = 0
	total_size_approx = 0
	for file in ["mar","apr","may","jun","jul","aug"]:
		total=0
		parsed=0

		file_name="airline_delay_data_%s_23.csv"%file

		print(f"\n{file_name}:")
		
		file_stats = os.stat(file_name)
		f_size = file_stats.st_size/(1000*1000)

		print(f"File size = {f_size:.2f} MB")

		with open(file_name,newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if (checkNot(row, key_headers[0], 0.00, float) \
				or (checkNot(row, key_headers[1], 0.00, float) and (checkGroup(row, key_headers[-3:-1], "BOS") or checkGroup(row, key_headers[-3:-1], "JFK") or checkGroup(row, key_headers[-3:-1], "DCA") or checkGroup(row, key_headers[-3:-1], "LAX"))) \
				) and (checkGroup(row, key_headers[-1:], "AA") or checkGroup(row, key_headers[-1:], "UA") or checkGroup(row, key_headers[-1:], "DL") or checkGroup(row, key_headers[-1:], "MQ")): 
					dataset.append(row)
					parsed +=1
				total +=1

		complete_data += parsed
		print(f"Total={total} \t Parsed={parsed}")

		compressed = parsed/total
		print(f"Compressed = {compressed:.3f} %")
		total_size_approx+=compressed*f_size

		# print("\t".join(key_headers)+"\n")

		# for data in dataset[:200]:
		# 	for key in key_headers:
		# 		print(f"{data[key]}\t\t",end='')

		# 	print("\n\n")

	print(f"\n\nTotal data size = {complete_data}")
	print(f"\nTotal size approx = {total_size_approx:.2f} MB")


	with open('airlines_delay_data.csv','w', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers,extrasaction='ignore')
		writer.writeheader()
		for data in dataset:
			writer.writerow(data)

	print(f"Pre process completed!!")


### Perform raw analysis
field_to_analyse=dict()

def analyse(file_name):

	with open(file_name,newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				dataset.append(row)
				addMap(airlines_to_filter,row["OP_UNIQUE_CARRIER"])
				addMap(origins_to_filter,row["ORIGIN"])
				addMap(dest_to_filter,row["DEST"])

	for data in dataset:
		addMap(field_to_analyse,data['DEP_DEL15'])

	# print(field_to_analyse)

	# print("\t".join(headers)+"\n")

	# print(f"\nAirlines\n")
	# for k, v in sorted(airlines_to_filter.items(), key=lambda item: item[1]):
	# 	print(f"{k} => {v}")

	# print("\n\n")
	# print(f"Origins\n")
	# for k,v in sorted(origins_to_filter.items(), key=lambda item: item[1]):
	# 	print(f"{k} => {v}")

	# print("\n\n")
	# print(f"Destination\n")
	# for k,v in sorted(dest_to_filter.items(), key=lambda item: item[1]):
	# 	print(f"{k} => {v}")	

if __name__ == '__main__':
	# preprocess()
	# analyse("airlines_delay_data.csv")







