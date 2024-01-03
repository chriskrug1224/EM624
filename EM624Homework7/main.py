# Author: Christopher Kruger
"""
Description:
Calculate and print the following:
o Number of courses per each program per each Academic Year
o Average number of courses per faculty per Academic Year
o Number of underloaded faculty per each Academic Year
o Number of overloaded faculty per each Academic Year

Make 4 Bokeh plots:
Courses per program per Academic Year.
Average number of courses per faculty over the years
Number of overloaded faculty over the years
Courses by program in '22-'23
"""

import pandas as pd
from math import pi
import numpy as np
import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

df = pd.read_csv("SSE_Faculty.csv") # Read in CSV
df.replace(np.nan,0, inplace = True) # Replaces N/A with zero if needed

# First Part
print('\n Part 1 \n')
firstYearTotal = df.groupby(["Program"])["Load 19-20"].agg("sum") # Sums up each program load using the Sum aggregate function
secondYearTotal = df.groupby(["Program"])["Load 20-21"].agg("sum")
thirdYearTotal = df.groupby(["Program"])["Load 21-22"].agg("sum")
fourthYearTotal = df.groupby(["Program"])["Load 22-23"].agg("sum")
print("Number of courses in the Academic Year 2019 - 2020 \n", firstYearTotal.to_string()) # Printing each Academic Year totals
print("Number of courses in the Academic Year 2020 - 2021 \n", secondYearTotal.to_string())
print("Number of courses in the Academic Year 2021 - 2022 \n", thirdYearTotal.to_string())
print("Number of courses in the Academic Year 2022 - 2023 \n", fourthYearTotal.to_string())

# Second Part
print("\n Part 2 \n")
firstIDMean = df.groupby(["ID"])["Load 19-20"].mean() # Finds the average for each faculty ID using the mean agregate function
secondIDMean = df.groupby(["ID"])["Load 20-21"].mean()
thirdIDMean = df.groupby(["ID"])["Load 21-22"].mean()
fourthIDMean = df.groupby(["ID"])["Load 22-23"].mean()
print("Average number of course per faculty ID in the Academic Year 2019 - 2020 \n", firstIDMean.to_string()) # Printing each faculty ID average course amount per academic year
print("Average number of course per faculty ID in the Academic Year 2020 - 2021 \n", secondIDMean.to_string())
print("Average number of course per faculty ID in the Academic Year 2021 - 2022 \n", thirdIDMean.to_string())
print("Average number of course per faculty ID in the Academic Year 2022 - 2023 \n", fourthIDMean.to_string())

# Third Part
print("\n Part 3 - Underloaded\n")
# Finding those that are underload/overload by using the Balance Column
firstYearBalance = df["Balance 19-20"]
secondYearBalance = df["Balance 20-21"]
thirdYearBalance = df["Balance 21-22"]
fourthYearBalance = df["Balance 22-23"]
# Checks how many were less than the target
firstYearUnderload = firstYearBalance[firstYearBalance < 0].count()
secondYearUnderload = secondYearBalance[secondYearBalance < 0].count()
thirdYearUnderload = thirdYearBalance[thirdYearBalance < 0].count()
fourthYearUnderload = fourthYearBalance[fourthYearBalance < 0].count()
# Prints underload values
print("Number of faculty who were underloaded in the Academic Year 2019 - 2020 \n", firstYearUnderload)
print("Number of faculty who were underloaded in the Academic Year 2020 - 2021 \n", secondYearUnderload)
print("Number of faculty who were underloaded in the Academic Year 2021 - 2022 \n", thirdYearUnderload)
print("Number of faculty who were underloaded in the Academic Year 2022 - 2023 \n", fourthYearUnderload)
# Checks how many were more than the target
print("\n Part 3 - Overloaded\n")
firstYearOverload = firstYearBalance[firstYearBalance > 0].count()
secondYearOverload = secondYearBalance[secondYearBalance > 0].count()
thirdYearOverload = thirdYearBalance[thirdYearBalance > 0].count()
fourthYearOverload = fourthYearBalance[fourthYearBalance > 0].count()
# Prints overload values
print("Number of faculty who were overloaded in the Academic Year 2019 - 2020 \n", firstYearOverload)
print("Number of faculty who were overloaded in the Academic Year 2020 - 2021 \n", secondYearOverload)
print("Number of faculty who were overloaded in the Academic Year 2021 - 2022 \n", thirdYearOverload)
print("Number of faculty who were overloaded in the Academic Year 2022 - 2023 \n", fourthYearOverload)

# Fourth Part
print("\n Part 4 \n")
print("Graphs will open in web browser...")

# First Graph - Courses Per Program Per Academic Year - Line Plot
output_file("Courses per Program per Academic Year.html")
graphOne = figure(title="Courses per Program per Academic Year")
graphOne.xaxis.axis_label = "Years"
graphOne.yaxis.axis_label = "Number of Courses"
# Plotting line 1 - EM
x = [19,20,21,22]
y = [39,29,48,52]
graphOne.line(x, y, line_color="blue", line_dash="solid", legend_label="EM")
# Plotting line 2 - SSW
x = [19,20,21,22]
y = [3,6,19,24]
graphOne.line(x, y, line_color="green", line_dash="solid", legend_label="SSW")
# Plotting line 3 - SYS
x = [19,20,21,22]
y = [28,28,31,22]
graphOne.line(x, y, line_color="yellow", line_dash="solid", legend_label="SYS")
show(graphOne)

# Second Graph - Average Number of Courses Per Faculty Over the Years - Bar Plot
output_file("Average Number of Courses per Faculty Over the Years.html")
# X Axis Points
ID = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27"]
# Parts of the inner bar graph
years = ["2019-2020", "2020-2021", "2021-2022", "2022-2023"]
data = {"ID": ID, "2019-2020": [6,0,3,2,2,0,2,1,0,3,2,6,0,6,5,6,2,0,0,2,9,2,0,2,0,0,9], "2020-2021": [4,0,3,3,3,0,3,2,0,1,3,7,0,3,3,1,3,1,1,2,6,3,0,3,0,0,8], "2021-2022": [8,1,3,2,3,0,3,4,2,3,2,4,3,9,6,9,3,1,5,2,6,5,1,1,0,7,5], "2022-2023": [8,2,3,3,4,5,3,3,4,2,1,0,2,5,5,8,2,2,3,2,3,4,2,4,5,5,8]}
graphTwo = figure(x_range = ID, height = 500, title = "Average Number of Courses per Faculty ID", toolbar_location = None, tools = "")
graphTwo.vbar_stack(years, x = 'ID', width = 0.9, color = ["orange", "green", "yellow","blue"], source = data, legend_label = years)
graphTwo.y_range.start = 0
graphTwo.x_range.range_padding = 0.1
graphTwo.xgrid.grid_line_color = None
graphTwo.axis.minor_tick_line_color = None
graphTwo.outline_line_color = None
graphTwo.legend.location = "top_left"
graphTwo.legend.orientation = "horizontal"
graphTwo.xaxis.axis_label = "Faculty ID"
graphTwo.yaxis.axis_label = "Number of courses"
show(graphTwo)

# Third Graph - Number of Overloaded Faculty Over the Years - Line Plot
output_file("Number of Overloaded Faculty Over the Years.html")
graphThree = figure(title = "Number of Overloaded Faculty Over the Years")
graphThree.xaxis.axis_label = "Years"
graphThree.yaxis.axis_label = "ID"
x = [20,21,22,23]
y = [4, 3, 7, 9]
line_color = "green"
line_dash = "solid"
graphThree.line(x, y, line_color = line_color, line_dash = line_dash)
show(graphThree)

# Fourth Graph - Courses Per Program in 2022 - 2023 - Pi Chart
output_file("Courses per Program in '22 - '23.html")
x = {"EM": 52, "SSW": 24, "SYS": 22}

data = pd.Series(x).reset_index(name = "value").rename(columns = {"index": "program"})
data["angle"] = (data["value"]) / (data["value"].sum()) * (2*pi)
data["color"] = ["blue", "green", "yellow"]
graphFour = figure(height = 500, title="Courses per Program in '22 - '23", toolbar_location = None, tools = "hover", tooltips = "@program: @value", x_range = (-0.5, 1.0))
graphFour.wedge(x = 0, y = 0, radius = 0.5, start_angle = cumsum("angle", include_zero = True), end_angle = cumsum("angle"), line_color = "black", fill_color = "color", legend_field = "program", source = data)
graphFour.axis.visible = False
show(graphFour)