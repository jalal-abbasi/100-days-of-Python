#import pandas

#data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"].tolist()
#
# average_temp = sum(temperatures)/len(temperatures)
# row = data[data.temp == data.temp.max()]

#1 first step: getting hold of an entire column
#entire_column = data["day"] # data[column_title]
#or

#entire_column = data.day

#2 second one: getting hold of an entire row
#entire_row = data[data.day == "Monday"]  #data[the elements of one a columns is equal to one specific value]

#3 third step: getting hold of an element in a row
#row = data[data.day == "Monday"] # first we get the row
#print(row["condition"]) or print(row.condition]) #then in that row we specify the column title of the desired element

#temp = data[data.day == "Monday"]["temp"]
#print(type(temp))

################ EXERCISE 2 ########################################

import pandas
sq_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sq_data_list = sq_data["Primary Fur Color"].tolist()

# colors = ['Gray', 'Cinnamon', 'Black']
# index = {'Gray': 0, 'Cinnamon': 0, 'Black': 0}
# values = []
# for color in colors:
#     for item in sq_data_list:
#         if item == color:
#             index[color] += 1
#     values.append(index[color])
#
# my_dictionary = {"Fur Color": colors,
#                  "Count": values}
# my_data = pandas.DataFrame(my_dictionary)
# my_data.to_csv("squirrel_count.csv")

colors = ['Gray', 'Cinnamon', 'Black']
counter = []
for color in colors:
    counter.append(sq_data_list.count(color))

my_dictionary = {"Fur Color": colors,
                 "Count": counter}
my_data = pandas.DataFrame(my_dictionary)
my_data.to_csv("squirrel_count.csv")

