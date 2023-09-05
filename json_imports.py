import json

json_file = open('friends_json.txt', 'r')
read_json = json.load(json_file)
json_file.close()

print(read_json['friends'])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file2 = open('cars.txt', 'w')
dump_file = json.dump(cars, file2)
file2.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])