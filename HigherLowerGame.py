import random
seedVal = int(input('What seed should be used? '))
random.seed(seedVal)

lower_bound = 1
upper_bound = 0
while upper_bound < lower_bound:
    lower_bound = int(input('What is the lower bound? '))
    upper_bound = lower_bound - 1
    upper_bound = int(input('What is the upper bound? '))
    if upper_bound < lower_bound:
        print('Lower bound must be less than upper bound.')

random_number = random.randint(lower_bound, upper_bound)
user_guess = random_number - 1
while random_number != user_guess:
    user_guess = int(input('What is your guess? '))
    if lower_bound <= user_guess <= upper_bound:
        if random_number > user_guess:
            print('Nope, too low.')
        elif random_number < user_guess:
            print('Nope, too high.')
    else:
        print('{} is outside the bounds!'.format(user_guess))

print('You got it!')
