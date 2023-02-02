username = input("Could you give me your name? ")
print(f"Welcome {username}!")
surname = input(f"Could you give me your surname {username}? ")
age = input(f"Could you give me your age {username}? ")
country = input(f"Could you give me your country {username}? ")

print(username, surname, age, country)


def return_number(x):
    if x > 0:
        return x % 10


return_number(15)
