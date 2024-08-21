# with open("weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# Using CSV library to work around CSV files
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# Pandas - Data Analysis Library
# import pandas
# from fontTools.merge.util import avg_int
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
# print(data["temp"].mean())
#
# print(data["temp"].max())

#Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# temp_to_f = (monday["temp"] * 9/5) + 32
# print(temp_to_f)

#Create a dataframe from scratch
# data_dict = {
#     "subjects": ["IS", "DSAP", "SPIT"],
#     "grade":["A","C-","A-"]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

s_grey_count = len(data[data["Primary Fur Color"] == "Gray"])
print(s_grey_count)
s_red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
s_black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["grey","red","black"],
    "Count":[s_grey_count, s_red_count, s_black_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")

