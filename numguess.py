from random import randint

# Create answer range: 1 to 100(integer)
answer = randint(1, 100)
# print answer(for debugging)
print(answer)


# get user's name, guess

user_name = input('Hello there, What's your name? ')
guess = int(input(f'Hi, {user_name}. Guess the number(1-199); '))

# print to check
print(user_name, guess)

# check and print correct not
if guess == answer:
    print('Congrats!')
else: 
    print(f'You are wrong' The answer is {answer}.')



