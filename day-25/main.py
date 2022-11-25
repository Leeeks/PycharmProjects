import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
white_squirrels_count = len(data[data["Primary Fur Color"] == "White"])

data_dict = {
    "Primary Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data_frame = pandas.DataFrame(data_dict)
new_data_frame.to_csv("squirrel_count.csv")