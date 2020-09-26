#!/usr/bin/env python3


def validPalindrome(s):

    i = 0
    j = len(s)-1

    while(i < j):
        if not s[i].isalnum():
            i += 1
            continue
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False

    return True

def main():
    print(validPalindrome('A man, a plan, a canal: Panama'))
    print(validPalindrome('race a car'))


if __name__ == '__main__':
    main()
