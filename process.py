# opens the txt file and saves content in variable "log_file"
log_file = open("um-server-01.txt")

def sales_reports(log_file):
    # loops through each line of the txt file
    for line in log_file:
        # removes any trailing characters
        line = line.rstrip()
        # takes the first three characters of the line (day of week) and assigns them to variable 'day'
        day = line[0:3]
        # if 'day' variable is "Mon", then print the contents of that line on the terminal
        if day == "Mon":
            print(line)

# calls the 'sales_reports' function with argument 'log_file'
sales_reports(log_file)
