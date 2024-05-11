from random import randint

def main():
    friends = {}
    number_of_friends = get_number_of_friends()
    print()

    if number_of_friends == 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends_list = []
    for _ in range(number_of_friends):
        name_of_friend = input()
        friends_list.append(name_of_friend)

    friends = dict.fromkeys(friends_list, 0)

    print()
    total_bill = get_total_of_bill()
    is_lucky_feature_used = get_is_lucky_feature_used()
    print()
    if is_lucky_feature_used == "Yes":
        index = randint(0, number_of_friends)
        lucky_friend = friends_list[index]
        print(f"{lucky_friend} is the lucky one!")
        split_bill(friends, total_bill, number_of_friends - 1, lucky_person=lucky_friend)
    elif is_lucky_feature_used == "No":
        print("No one is going to be lucky")
        split_bill(friends, total_bill, number_of_friends)



def get_number_of_friends():
    number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

    return number_of_friends if number_of_friends >= 1 else 0


def get_total_of_bill():
    return int(input("Enter the total bill value\n"))


def split_bill(friends, total_bill, number_of_friends, lucky_person=""):
    print()
    friends = {friend: round(total_bill / number_of_friends, 2) for friend in friends}
    if lucky_person != "":
        friends[lucky_person] = 0
    print(friends)


def get_is_lucky_feature_used():
    return input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")


main()