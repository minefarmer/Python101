person = {
    "key": "value",
    "name": "Carl",
    "github": "minefarmer"
}
print(person['github'])  # minefarmer

print(person)  # {'github': 'minefarmer', 'name': 'Carl', 'key': 'value'}

person['instagram'] = "@coding for everybody"
print(person)  # {'github': 'minefarmer', 'name': 'Carl', 'key': 'value', 'instagram': '@coding for everybody'}

del person['key']
print(person)  # {'github': 'minefarmer', 'name': 'Carl', 'instagram': '@coding for everybody'}  #  'key': 'value' was deleted
