# Open the file in read mode ('r')
with open('euphoria_data.csv', 'r') as file:
    # The 'with' statement automatically closes the file when the block ends

    # Read the header line (column names)
    header = file.readline()

    # Read the rest of the lines

    big_list = []
    for line in file:
        # Process each line here
        # print(line)  # This will print each line with newline characters

        # To remove whitespace and newline characters:
        clean_line = line.strip()
        # print(clean_line)
        # Split the line into values using comma as separator
        columns = clean_line.split(',')

        #Big list of the colums list which was already separated by commas.

        big_list.append(columns)





# Initialize a dictionary to store statistics for each algorithm
stats = {
    'JoyStream': { 'total_happiness': 0, 'total_duration': 0, 'session_count': 0 },
    'SerenityFlow': { 'total_happiness': 0, 'total_duration': 0, 'session_count': 0 },
    'DeepPulse': { 'total_happiness': 0, 'total_duration': 0, 'session_count': 0 }
}

joystream_count = 0
serenityflow_count = 0
deeppulse_count = 0 

for user in big_list:
    if user[1] == "JoyStream":
        joystream_count = joystream_count + 1
    if user [1] == "SerenityFlow":
        serenityflow_count = serenityflow_count + 1 
    if user [1] == "DeepPulse":
        deeppulse_count = deeppulse_count + 1

stats["JoyStream"]["session_count"] = joystream_count 
stats ["SerenityFlow"]["session_count"] = serenityflow_count
stats ['DeepPulse']["session_count"]= deeppulse_count

joystream_duration = 0
serenityflow_duration  = 0
deeppulse_duration  = 0 

for user in big_list:
    if user[1] == "JoyStream":
        joystream_duration += int(user[2])
    if user [1] == "SerenityFlow":
        serenityflow_duration += int(user[2])
    if user [1] == "DeepPulse":
        deeppulse_duration += int(user[2])


stats['JoyStream'] ["total_duration"] = joystream_duration
stats ["SerenityFlow"] ["total_duration"] = serenityflow_duration
stats ["DeepPulse"] ["total_duration"] = deeppulse_duration

js_h = 0
sf_h = 0
dp_h = 0

for user in big_list:
    if user [1] == "JoyStream":
        js_h +=int(user [3])
    if user [1] == "SerenityFlow":
        sf_h += int(user [3])
    if user [1] == "DeepPulse":
        dp_h += int(user[3])

stats ["JoyStream"] ["total_happiness"]= js_h
stats ["SerenityFlow"] ["total_happiness"] = sf_h
stats ["DeepPulse"] ["total_happiness"] = dp_h

js_avg_h = stats ["JoyStream"] ["total_happiness"] / stats["JoyStream"]["session_count"]
js_avg_d = stats ["JoyStream"] ["total_duration"] / stats["JoyStream"]["session_count"]

sf_avg_h = stats ["SerenityFlow"] ["total_happiness"] / stats["SerenityFlow"]["session_count"]
sf_avg_d = stats ["SerenityFlow"] ["total_duration"] / stats["SerenityFlow"]["session_count"]

dp_avg_h = stats ["DeepPulse"] ["total_happiness"] / stats["DeepPulse"]["session_count"]
dp_avg_d = stats ["DeepPulse"] ["total_duration"] / stats["DeepPulse"]["session_count"]

print('Euphoria User Engagement Analysis Report')
print('----------------------------------------\n')

print('Average Happiness Rating per Algorithm:')
print(f'- JoyStream: {js_avg_h:.2f}')
print(f'- SerenityFlow: {sf_avg_h:.2f}')
print(f'- DeepPulse: {dp_avg_h:.2f}\n')

print('Total Number of Sessions per Algorithm:')
print(f'- JoyStream: {stats["JoyStream"]['session_count']}')
print(f'- SerenityFlow: {stats["SerenityFlow"]['session_count']}')
print(f'- DeepPulse: {stats["DeepPulse"]['session_count']}\n')

print('Average Session Duration per Algorithm:')
print(f'- JoyStream: {js_avg_d:.2f} minutes')
print(f'- SerenityFlow: {sf_avg_d:.2f} minutes')
print(f'- DeepPulse: {dp_avg_d:.2f} minutes\n')

print('Highest Average Happiness Rating:')
if (js_avg_h > sf_avg_h):
    if (js_avg_h > dp_avg_h):
        print(f"- JoyStream with an average happiness rating of {js_avg_h:.2f}\n")
    else:
        print(f"- DeepPulse with an average happiness rating of {dp_avg_h:.2f}\n")
else:
    if (sf_avg_h > dp_avg_h):
        print(f"- SerenityFlow with an average happiness rating of {sf_avg_h:.2f}\n")
    else:
        print(f"- DeepPulse with an average happiness rating of {dp_avg_h:.2f}\n")

print('Longest Average Session Duration:')
if (js_avg_d > sf_avg_d):
    if (js_avg_d > dp_avg_d):
        print(f'- JoyStream with an average session duration of {js_avg_d:.2f} minutes')
    else:
        print(f'- DeepPulse with an average session duration of {dp_avg_d:.2f} minutes')
else:
    if (sf_avg_d > dp_avg_d):
        print(f'- SerenityFlow with an average session duration of {sf_avg_d:.2f} minutes')
    else:
        print(f'- DeepPulse with an average session duration of {dp_avg_d:.2f} minutes')





    
        

