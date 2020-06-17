import datetime

name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
display_msg = int(input('Number of times you want to see the messages: '))


if age <= 100:
    age_100 = 100 - age
    now = datetime.datetime.now()
    age_100_year = now.year + age_100
    for i in range(display_msg):
        print('{} will be 100 in {} years'.format(name, age_100))
    print('In {} you will be 100 years old.'.format(age_100_year))

