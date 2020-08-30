#!/usr/bin/env python3

def remove_char(s, c):
    out = []
    for item in s:
        if item !=c:
            out.append(item)
    return out

def main():
    s = input("Enter the string: ")
    c = input("Enter the char you want to remove: ")

    out = remove_char(s, c)
    print(out)

if __name__ == '__main__':
    main()


