lst = ["String", 1, 3.14, ["A new item", "old item"], "Richard"]
print(lst)  # ['String', 1, 3.14, ['A new item'], 'Richard']

for item in lst:
    print(item)  # String
                # 1
                # 3.14
                # ['A new item', 'old item']
                # Richard


>>> names = ["Carl", "Rich"]
>>> names
['Carl', 'Rich']
>>> names.append("Sis")
>>> names
['Carl', 'Rich', 'Sis']
>>> names.remove('Carl')
>>> names
['Rich', 'Sis']
>>>  Sue = names.pop()
>>> names
['Rich']
>>> Sue
'Sis'
>>> 
