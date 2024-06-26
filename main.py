# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # # sum_temp = 0.0
# # # counter = 1
# # print(temp_list)
# # # for temp in temp_list:
# # #     sum_temp+=temp
# # #     counter+=1
# # # ave_temp = sum_temp / counter
# # # print(f"Average temperature: {ave_temp}")
# #
# # # ave_temp = sum(temp_list) / len(temp_list)
# # # print(ave_temp)
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # #Get Data in Columns
# # print(data.condition)
#
# # #Get Data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Data frame from scratch
# data_dict = {
#     "students": ["Ruffa", "Ela", "Ruffino"],
#     "scores": [75, 80, 95]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
#############################################################################
import pandas

data = pandas.read_csv("squirrel_data2018.csv")
color_list = data["Primary Fur Color"]
color_dict = {}
count = 0
for color in color_list:
    if color not in color_dict.keys():
        color_dict[color] = count + 1
    elif color in color_dict.keys():
        count = color_dict[color] + 1
        color_dict[color] = count
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_dict["Gray"], color_dict["Cinnamon"], color_dict["Black"]]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")




