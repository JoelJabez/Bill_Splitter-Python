def main():
    friends = {}
    number_of_friends = get_number_of_friends()
    print()

    if number_of_friends == 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        name_of_friend = input()
        friends[name_of_friend] = 0

    print(friends)


def get_number_of_friends():
    number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

    return number_of_friends if number_of_friends >= 1 else 0


main()