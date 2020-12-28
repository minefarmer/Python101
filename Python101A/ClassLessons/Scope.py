# def myfunc():
#     name = "Rich"

# print(name)  # Traceback (most recent call last):  #@# print is outside of the scope of the function
#             # File "/home/rich/CarlsHub/Python101/ClassLessons/Scope.py", line 4, in <module>
#             #     print(name)
#             # NameError: name 'name' is not defined


# def myfunc():
#     name = "Rich"
#     return name

# myfunc()
# print(name)    # Traceback (most recent call last):  #@# print is outside of the scope of the function
#                 # File "Scope.py", line 15, in <module>
#                 #     print(name)  
#                 # NameError: name 'name' is not defined


# name = "Rich"
# def myfunc():
#     return name

# print(myfunc())  # Rich


# name = "Rich"
# def myfunc():
#     name = "New name"
#     return name

# print(myfunc())  # New name
# print(name)  # Rich


# This will look for a name anywhere above the function either way print is written.
name = "Rich"
def myfunc():
    return name

print(myfunc())  # Rich
print(name)  # Rich

