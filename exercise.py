import json

csv_file = open('csv_file.txt', 'r')
my_dict = []
csv_file = [line.strip() for line in csv_file]
for line in csv_file:
    club,city,country = line.split(',')
    team = {
        'club': club,
        'city': city,
        'country': country
    }
    my_dict.append(team)

json_file = open('json_file.txt', 'w')
json.dump(my_dict, json_file)
json_file.close()