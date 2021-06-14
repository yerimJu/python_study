import csv

def get_key(item):
    return item[1]

command_data = []
with open("command_data.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="\"")
    for row in spamreader:
        command_data.append(row)

print(command_data[3])

command_counter = {}
for data in command_data:
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

dict_list = []
for k, v in command_counter.items():
    dict_list.append([k, v])

sorted_dict = sorted(dict_list, key=get_key, reverse=True)
print(sorted_dict[:100])
