# Author: Christopher Kruger
# Homework 3
# This program will process two different CSV files regarding NYC Citi Bike data from different time lines, and compare the two data sets

# These variables are for Jan_Feb
TotalLinesJF = 0
TotalCustomersJF = 0
TotalSubscribersJF = 0
PercentCustJF = 0
# These variables are for Apr_May
TotalLinesAM = 0
TotalCustomersAM = 0
TotalSubscribersAM = 0
PercentCustAM = 0
# These variables are used in the print command at the end for comparisons between the two files
JFBigger = 'smaller'
JFPercBigger = 'smaller'
# Part 1/File 1
with open('NYC-CitiBike-Jan_Feb2016.csv', 'r') as in_file1: # Opening the file
    lines = in_file1.readlines() # Reading the file
    for line in lines[1:]: # Skips the first line because it is the header
        info = line.strip().split(',') # Removes all whitespace and seperates by comma
        TotalLinesJF += 1 # Adding to the total line count
        if info[13] == "Customer": # 13th column is where it signifies if it is a customer or subscriber
            TotalCustomersJF += 1
        elif info[13] == "Subscriber":
            TotalSubscribersJF += 1
    print("These are the last five lines in the file:\n")
    for line in lines[-5:]: # Prints the last five lines
        print(line)
    print("\n")
PercentCustJF = (TotalCustomersJF / TotalLinesJF) * 100 # Percent calculation
print("The file has", TotalLinesJF, "lines. Of those,", TotalCustomersJF, "have usertype as 'Customer',", TotalSubscribersJF, "have usertype as 'Subscriber'. 'Customer' are", PercentCustJF, "% of the total. \n")

# File 2/Part 2
with open('NYC-CitiBike-Apr_May2016.csv', 'r') as in_file2: # Opening the file
    lines = in_file2.readlines() # Reading the file
    for line in lines[1:]: # Skips the first line because it is the header
        info = line.strip().split(',') # Removes all whitespace and seperates by comma
        TotalLinesAM += 1 # Adding to the total line count
        if info[13] == "Customer": # 13th column is where it signifies if it is a customer or subscriber
            TotalCustomersAM += 1
        elif info[13] == "Subscriber":
            TotalSubscribersAM += 1
    print("These are the first five lines in the file:\n")
    for line in lines[1:6]: # Prints the first five lines, skipping the header
        print(line)
    print("\n")
print("The file has", TotalLinesAM, "lines, of which", TotalCustomersAM, "have usertype 'Customer',", TotalSubscribersAM, "have usertype as 'Subscriber' \n")
PercentCustAM = (TotalCustomersAM / TotalLinesAM) * 100 # Percent calculation
if (TotalLinesJF > TotalLinesAM): # Adjusting the original string to make better sense in the full sentence
    JFBigger = 'larger'
if (PercentCustJF > PercentCustAM): # Adjusting the original string to make better sense in the full sentence
    JFPercBigger = 'larger'
print("The first file is", JFBigger, "than the second one. The percentage of Customer in the first file is", JFPercBigger, "than in the second one\n") # Overview of the two files, adjusted based on which is bigger
# Part 3
if (TotalLinesJF > TotalLinesAM): # Comparison between which file is bigger
    print("The Winter riders are more than the Spring\n")
else:
    print("The Spring riders are more than the Winter\n")
if (PercentCustJF > PercentCustAM): # Comparison between which file has a more Customer percentage
    print("During the Winter there are more Customers/non-Subscribers than in the Spring\n")
else:
    print("During the Spring there are more Customers/non-Subscribers than in the Winter\n")