# Tuples
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apple', 'Bananas', 'Grapes'))
fruits2 = ('Apples',)
# must have trailing comma with single value or thinks it's a string
del fruits2
# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}
# print(type(fruits_set))
# print('Apples' in fruits_set)
fruits_set.add('Grape')
fruits_set.remove('Grape')
# Dictionaries
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
# print(person, type(person))
# print(person['first_name'])
person['phone'] = '333-333-3333'
print(person.keys())
del(person['age'])
person.pop('phone')