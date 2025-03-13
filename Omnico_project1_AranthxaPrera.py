# Open the file in read mode ('r')
with open('euphoria_data.csv', 'r') as file:
    # The 'with' statement automatically closes the file when the block ends

    # Read the header line (column names)
    header = file.readline()

    # Read the rest of the lines
    for line in file:
        # Process each line here
        print(line)  # This will print each line with newline characters

        # To remove whitespace and newline characters:
        clean_line = line.strip()
        print(clean_line)
        # Split the line into values using comma as separator
        columns = line.split(',')
   
# Convert string to integer
session_duration = int(columns[2])

# Convert string to float (for decimal numbers)
happiness_rating = int(columns[3])



# # Initialize a dictionary to store statistics for each algorithm
# stats = {
#     'JoyStream': {
#         'total_happiness': 0,
#         'total_duration': 0,
#         'session_count': 0
#     },
#     'SerenityFlow': {
#         'total_happiness': 0,
#         'total_duration': 0,
#         'session_count': 0
#     },
#     'DeepPulse': {
#         'total_happiness': 0,
#         'total_duration': 0,
#         'session_count': 0
#     }
# }


