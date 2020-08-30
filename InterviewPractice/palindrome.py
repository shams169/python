#!/usr/bin/env python3


def is_palindrome(val):
    if val[::-1] == val:
        print('The string is palindrome')
    else:
        print('The string is not a PALINDROME')



def main():
    val = input("Enter a value to check: ")
    is_palindrome(val)
if __name__ == '__main__':
    main()