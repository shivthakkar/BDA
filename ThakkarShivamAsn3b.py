# Shivam Thakkar Assignment 3b 

def is_palindrome(str):
    updated_str = ''
    for char in str:
        if char.isalpha():
            updated_str += char
    updated_str = updated_str.lower()
    if updated_str == updated_str[::-1]:
        return True
    else:
        return False

while True:
    str = input('Please enter a word or phrase, or to quit: ')
    if str == '':
        break
    else:
        if is_palindrome(str):
            print("That's a palindrome")
        else:
            print("That's not a palindrome")

