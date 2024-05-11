def get_age(name, ages):
    try:
        return ages[name]
    except KeyError:
        return "Not found"

name = input()
ages = eval(input())
print(get_age(name, ages))