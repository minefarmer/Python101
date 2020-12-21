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



# def somename(name=None, food="Pizza"):
#     if name is None:
#         name = "Zephyer" 

#     person_type = "human"
#     if name == "Zephyer":
#         person_type = "Cat"  # Cat

#     print(person_type)

#     print(f"Hello {name}. Let's eat some {food}.")  # Hello Zephyer. Let's eat some Pizza.

# somename()


def somename(name=None, food="Pizza"):
    if name is None:
        name = "Zephyer" 

    person_type = "human"
    if name == "Zephyer":
        person_type = "Cat"

    print(person_type)   # Cat

    print(f"Hello {name}. Let's eat some {food}.")  # Hello Zephyer. Let's eat some Pizza.

some_var = somename()

print(f"The variable is ", some_var)  # The variable is  None


# def somefunction():
#     return "a value"

# thing = somefunction()
# print(thing)  # a value


# def exp(num1, num2):
#     total = num1 ** num2   
#     return total

# big_number = exp(33, 6)
# print(big_number)  # 1291467969
