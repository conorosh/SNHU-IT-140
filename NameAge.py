import datetime

now = datetime.datetime.now()
name = input('What is your name?')
age = int(input('How old are you? '))
print('Hello {}! You were born in {}.'.format(name, str(now.year - age)))
