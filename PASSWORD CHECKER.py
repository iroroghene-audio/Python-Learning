#PASSWORD CHECKER

password = '123456'

user_input = input('Please enter your password: ')
count = 0
while password != user_input:
    count += 1
    user_input = input('Password Incorrect! Please re-enter the correct password: ')

    if count == 5:
        print('Too many attempts. Please try again later.')
        break
else:
    print('Login Successful!')