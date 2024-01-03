'''
    Author: Christopher Kruger
    Description: This code will parse through the two given csv files to give statistics,
    such as total custommers/subscribers, most used stations, etc.
'''
import pandas as pd
from datetime import datetime
# Import two CSV files into Pandas Dataframe
file1 = "JC-201611-citibike-tripdata.csv"
file2 = "JC-202111-citibike-tripdata.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

#Initialize at top so I can use it outside the function
subscriber_count1 = 0
customer_count1 = 0
subscriber_count2 = 0
customer_count2 = 0
def print_details(df):
    # Variables needed for File1
    avgDuration1 = 0
    totalTrip1 = 0
    subscriber_count1 = 0
    customer_count1 = 0
    start_station_counts1 = {}
    end_station_counts1 = {}
    # Variables needed for File2
    totalTrip2 = 0
    subscriber_count2 = 0
    customer_count2 = 0
    start_station_counts2 = {}
    end_station_counts2 = {}

    if (df.columns[0] == "Trip Duration"): # Tells me which file is open, if true then it is File1. Otherwise, File2
        print("For File1: \n")
        for index, row in df.iterrows(): # For all calculations
            totalTrip1 += row[0] # Adding up the total minutes of trip durations
            start_station = row["Start Station Name"] # Identify the start stations based off the column Start Station Name
            end_station = row["End Station Name"] # Identify the end stations based off the column End Station Name
            if start_station not in start_station_counts1: # For the count of each start station
                start_station_counts1[start_station] = 1
            else:
                start_station_counts1[start_station] += 1
            if end_station not in end_station_counts1: # For the count of each end station
                end_station_counts1[end_station] = 1
            else:
                end_station_counts1[end_station] += 1
            user_type = row["User Type"] # Checking for total count of Subscriber vs Customer
            if user_type == "Subscriber":
                subscriber_count1 += 1
            elif user_type == "Customer":
                customer_count1 += 1
        avgDuration1 = totalTrip1 / len(df) / 60 # Calculates the average duration
        # End of calculation. Now does print logic
        print("The average daily trip duration for File1 is:", avgDuration1, "minutes!")
        # Finding the five most popular stations for start and end
        popular_start_stations = sorted(start_station_counts1.items(), key=lambda x: x[1], reverse=True)[:5] # From ChatGPT
        popular_end_stations = sorted(end_station_counts1.items(), key=lambda x: x[1], reverse=True)[:5] # From ChatGPT
        print("\nThe five most used start stations are: ")
        for station, count in popular_start_stations:
            print(f"{station}: {count} times")
        print("\nThe five most used end stations are: ")
        for station, count in popular_end_stations:
            print(f"{station}: {count} times")
        print("\nSubscriber Count: ", subscriber_count1)
        print("\nCustomer Count: ", customer_count1)
    else:
        print("\nFor File2: \n")
        start_time = '' # Used if I got my duration calculation right
        end_time = '' # Used if I got my duration calculation right
        for index, row in df.iterrows():
            start_station = row["start_station_name"] # Identify the start stations based off the column start_station_name
            end_station = row["end_station_name"] # Identify the end stations based off the column end_station_name
            if start_station not in start_station_counts2: # For the count of each start station
                start_station_counts2[start_station] = 1
            else:
                start_station_counts2[start_station] += 1
            if end_station not in end_station_counts2: # For the count of each end station
                end_station_counts2[end_station] = 1
            else:
                end_station_counts2[end_station] += 1
            user_type = row["member_casual"] # Checking for total count of Subscriber vs Customer
            if user_type == "member":
                subscriber_count2 += 1
            elif user_type == "casual":
                customer_count2 += 1
            # I WAS UNABLE TO COMPLETE THIS PART, BUT THE LOGIC SHOULD BE RIGHT! I COULDN'T FIGURE OUT WHAT WAS WRONG :(((
            # This is for calculating the duration between trips
            """
            start_time = datetime.strptime(row["started_at"], "%m/%d/%y %H:%M:%S") # Something is wrong with the month/day/year hour/minute/second format
            end_time = datetime.strptime(row["ended_at"], "%m/%d/%y %H:%M:%S")
            # Calculate the time difference in minutes
        time_difference = (end_time - start_time).total_seconds() / 60
        print(f"Trip duration: {time_difference} minutes")
            """
        # End of calculation. Now does print logic
        # Finding the five most popular stations for start and end
        popular_start_stations = sorted(start_station_counts2.items(), key=lambda x: x[1], reverse=True)[:5]
        popular_end_stations = sorted(end_station_counts2.items(), key=lambda x: x[1], reverse=True)[:5]
        print("\nThe five most used start stations are: ")
        for station, count in popular_start_stations:
            print(f"{station}: {count} times")
        print("\nThe five most used end stations are: ")
        for station, count in popular_end_stations:
            print(f"{station}: {count} times")
        print("\nSubscriber Count: ", subscriber_count2)
        print("\nCustomer Count: ", customer_count2)

print_details(df1)
print_details(df2)
if (subscriber_count1 < subscriber_count2 and customer_count1 < customer_count2):
    print ("The ridership in 2016 was higher for both customers and subscribers!")
else:
    print("The ridership in 2021 was higher for both customers and subscribers!")
print("This is the end of the files procesing")