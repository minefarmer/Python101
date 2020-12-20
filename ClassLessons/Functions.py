# name = "Rich"

# def somename():
#     print(f"Hello {name}")

# somename()  # Hello Rich


# def somename(name, food):
#     print(f"Hello {name}. Let's eat some {food}.")

# somename('Rich', 'tacos')  # Hello Rich. Let's eat some tacos.


# def somename(name, food="Pizza"):
#     print(f"Hello {name}. Let's eat some {food}.")

# somename('Rich', 'Oranges')  # Hello Rich. Let's eat some Oranges.


# def somename(name, food="Pizza"):
#     if name.lower() == "rich":
#         print("Welcome Rich")  # Welcome Rich
#     print(f"Hello {name}. Let's eat some {food}.")

# somename('Rich', 'Oranges')  # Hello Rich. Let's eat some Oranges.



def somename(name=None, food="Pizza"):
    if name is None:
        name = "Zephyer" 

    person_type = "human"
    if name == "Zephyr":
        person_type = "Cat"

    print(person_type)

    print(f"Hello {name}. Let's eat some {food}.")

somename()
