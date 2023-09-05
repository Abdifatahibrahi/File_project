csv_file = open('csv_data.txt', 'r')
lines = csv_file.readlines()
csv_file.close()

lines = [line.strip() for line in lines[1:]]


for line in lines:
    line_data = line.split(',')
    name = line_data[0].title()
    age = line_data[1]
    university = line_data[2].title()
    degree = line_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}')
