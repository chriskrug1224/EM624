# Author: Christopher Kruger
# Description:
# 1. numerically compare (no graph required) the percentage of courses online vs in-person (from the column "Delivery Mode").
# 2. numerically compare (no graph required) the level of courses (from the column "Level").
# 3. calculate the average enrolment (from the column "Enrollment Count"), printing the courses with less than 10 students and those with more than 30 students.
import pandas as pd

# Variables for part 1
coursesInPerson = 0
coursesOnline = 0
totalCourses = 0
# Variables for part 2
countCourseUG = 0
countCourseG = 0
countCourseCORP = 0
# Variables for part 3
averageEnrollment = 0
countEnrollmentSmall = 0
countEnrollmentLarge = 0

file_path = "REG_CAP_Spring22_624.csv"
df = pd.read_csv(file_path)

# --- Part A ---
delivery_mode = df["Delivery Mode"].value_counts()
totalCourses = len(df) # Total courses is the amount of rows
coursesOnline = (delivery_mode.get('Online', 0) / totalCourses) * 100 # Looks for online courses, then converts to percentage
coursesInPerson = (delivery_mode.get('In-Person', 0) / totalCourses) * 100 # Looks for in-person courses, then converts to percentage
# Printing for Part A
print("PART A:\n")
print("The percent of online courses is: ", round(coursesOnline,2), "%" ) # Rounding for readability
print("The percent of in-person courses is: ", round(coursesInPerson,2), "%") # Rounding for readability
print("----\n")

# --- Part B ---
level_of_course = df["Level"].value_counts()
# Gets the number of courses per UG, G, and CORP
countCourseUG = level_of_course.get("UG", 0)
countCourseG = level_of_course.get("G", 0)
countCourseCORP = level_of_course.get("CORP", 0)
print("Part B:\n") # Printing raw number of courses per category
print("There are", countCourseUG, "undergraduate courses")
print("There are", countCourseG, "graduate courses")
print("There are", countCourseCORP, "corporate courses")
# Checks which is more
if countCourseUG > countCourseG and countCourseUG > countCourseCORP:
    print("Undergraduate courses are the most provided type of course!")
elif countCourseG > countCourseUG and countCourseG > countCourseCORP:
    print("Graduate courses are the most provided type of course!")
elif countCourseCORP > countCourseUG and countCourseCORP > countCourseG:
    print("Corporate courses are the most provided type of course!")
print("----\n")

# --- Part C ---
averageEnrollment = df["Enrollment Count"].mean()
countEnrollmentSmall = len(df[df['Enrollment Count'] < 10])
countEnrollmentLarge = len(df[df["Enrollment Count"] > 30])
print("Part C:\n")
print("The average enrollment count is", averageEnrollment, "students")
print("There are", countEnrollmentSmall, "courses with less than 10 students")
print("There are", countEnrollmentLarge, "courses with more than 30 students")
print("----\n")
