#                                RANGE
countries = ['Nigeria', 'Ghana', 'Egypt']

for item in countries:
    print(item + ' is a country in West-Africa')
if item == 'Nigeria':
    print('yes, Nigeria is a country in West-Africa')
else:
    pass

print(len(countries))


numbers = list(range(1, 100))
print(numbers)

co_programmers = ['Michelle', 'Lizzy', 'Siyammama', 'Timayo', 'Toluwani', 'Tosin', 'Michael', 'Habib', 'Boyowa', 'Obafemi']

for people in co_programmers:
    print(people + ' is present!')
if people == 'Joyce':
    print('Joyce is here!')
else:
    print('Where is Joyce')
