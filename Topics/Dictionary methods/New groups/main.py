# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
groups_dict = dict.fromkeys(groups)

groups_to_be_filled = int(input())

for index in range(groups_to_be_filled):
    number = int(input())
    groups_dict[groups[index]] = number


print(groups_dict)