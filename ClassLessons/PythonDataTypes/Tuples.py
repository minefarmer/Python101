# Lists are changeable (mutable)
# Tuples are not changeable (immutable)


# # a list
# >>> animals = ['Cat', "Dog", 'Zebra', "Aardvaark"]
# >>> animals.sort()
# >>> animals
# ['Aardvaark', 'Cat', 'Dog', 'Zebra']

# a Tuple
# >>> foods = ('Pizza', 'Orange', 'Apple', 'Pasta',)  # add last comma so python knows for sure it is a tuple
# >>> type(foods)
# <class 'tuple'>
# >>> 


#  use foods.  Tab for list
# >>> foods
# ('Pizza', 'Orange', 'Apple', 'Pasta')
# >>> foods.
# foods.count(  foods.index(  
# >>> animals.
# animals.append(   animals.copy(     animals.extend(   animals.insert(   animals.remove(   animals.sort(     
# animals.clear(    animals.count(    animals.index(    animals.pop(      animals.reverse(  

# >>> foods.sort()     # tuples can't be sorted because they are immutable
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'sort'
# >>> 

foods = ('Pizza', 'Fish', 'Tomatoes',)
for food in foods:
    print("The food is", food)  # ('The food is', 'Pizza')
                                # ('The food is', 'Fish')
                                # ('The food is', 'Tomatoes')
