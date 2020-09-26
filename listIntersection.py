def listInterSection(l1, l2):
    return list(set(l1).intersection(set(l2)))

def main():
    print(listInterSection([15, 9, 10, 56, 23, 78, 5, 4, 9], [9, 4, 5, 36, 47, 26, 10, 45, 87]))

if __name__ == '__main__':
    main()