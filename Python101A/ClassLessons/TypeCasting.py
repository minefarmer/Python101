# str list bool dict tuple list tuple
# this is normal text

# age = input("What is your age? ")  # 82
# data_type = type(age)  # data type is equal to function type
# print(data_type)  # <class 'str'>

# # casting age  *** turning it into an integer
# age = int(age)  # 82
# data_type = type(age)
# print(data_type)  # <class 'int'>

# print("Your age in dog years is", (age * 7))  # Your age in dog years is 574


grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
grocery_list = set(grocery_list)
print(grocery_list)  # set(['Apples', 'Oranges', 'Bananas'])
print(type(grocery_list))  # <type 'set'>


grocery_list = ['Apples', 'Oranges', 'Bananas', 'Apples']
grocery_list = tuple(grocery_list)
print(grocery_list)  # ('Apples', 'Oranges', 'Bananas', 'Apples')
print(type(grocery_list))  # <type 'tuple'>
