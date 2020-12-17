# lst = [varname, varname2, varname3, varname4]
# dictionary = {
#     "key": "value",
# }
s = {"Item 1", "Item 2", "Item 3"}
print(s)  # set(['Item 3', 'Item 2', 'Item 1'])  === it does not care about the order.

s = {"Item 1", "Item 2", "Item 2", "Item 3"}
print(s)  # set(['Item 3', 'Item 2', 'Item 1'])


>>> s = {"Item 1", "Item 2", "Item 2", "Item 3"}
>>> s
{'Item 1', 'Item 3', 'Item 2'}
>>> s.
s.add(                          s.discard(                      s.issuperset(                   s.union(
s.clear(                        s.intersection(                 s.pop(                          s.update(
s.copy(                         s.intersection_update(          s.remove(                       
s.difference(                   s.isdisjoint(                   s.symmetric_difference(         
s.difference_update(            s.issubset(                     s.symmetric_difference_update(  
>>> s
{'Item 1', 'Item 3', 'Item 2'}
>>> s = {"Item 1", "Item 2", "Item 2", "Item 3"}
>>> s
{'Item 1', 'Item 3', 'Item 2'}
>>> s.add("Item 4")
>>> s
{'Item 1', 'Item 4', 'Item 3', 'Item 2'}
>>> s.remove("Item 3")
>>> s
{'Item 1', 'Item 4', 'Item 2'}
>>> 