###Python programm to find the number of request and status code in each minutes####
#Declare empty List.
parsed_data = []

#Read the log file as read noly
with open("logformat.log","r") as file:
    prev_time = ""
    data = {}
    #Read each line and split the time stamp and respective status code 
    for line in file:
        time = line.split("[")[1].split("]")[0].split(" ")[0]
        status_code = line.split('"')[2].split(" ")[1]
        if prev_time != "":
        	if prev_time == time:
        		data[time]["Request"] = data[time]["Request"] +1
        		if status_code in data[time]:
        			data[time][status_code] = data[time][status_code] +1
        		else:
        			data[time][status_code] = 1
        	else:
        		parsed_data.append(data)
        		data = {}
        		data[time] = {"Request": 1, status_code: 1}
        		prev_time = time
        else:
        	data[time] = {"Request": 1, status_code: 1}
        	prev_time = time

for out in parsed_data:
	print(out)
