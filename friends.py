

friends = input('Enter three friends separated by comas: ')
print(friends)
friends = friends.split(',')

people_file = open('people.txt', 'r')
people = [person.strip() for person in people_file.readlines()]


print(people)
people_file.close()

nearby_friends = open("nearby_friends.txt", 'w')
for friend in friends:
    if friend in people:
        nearby_friends.write(friend)
        nearby_friends.write('\n')

nearby_friends.close()





