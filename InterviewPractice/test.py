def sum(*args):
    total = 0
    for item in args:
        total += item

    return total



def main():
    print(sum(1,2,3,44,56))
    print(sum(4,6,73,73,8,44,88))
    print(sum([1,2,3,4]))


if __name__ == '__main__':
    main()