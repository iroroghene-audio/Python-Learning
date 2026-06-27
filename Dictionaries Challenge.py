user = {
    'id': 1,
    'name': 'John',
    'age': 30,
    'city': 'Berlin'
}

modified_user_dict = {}

for key, value in user.items():
    if type(value) is str:
      modified_user_dict[key] = value
print(modified_user_dict)