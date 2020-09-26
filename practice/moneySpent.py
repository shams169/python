def moneySpent(money, keys, usbs):

    count_min = min(keys, usbs)
    max_sum = []

    if len(keys) <= len(usbs):
        low = keys
        high = usbs
    else:
        low = usbs
        high = keys

    for x in low:
        for y in high:
            print(x, y)
            if x+y <= money:
                max_sum.append((x+y))
            else:
                break
    if not max_sum:
        return -1
    else:
        return max(max_sum)

def main():
    print(moneySpent(10, [3,1], [5,2,8]))


if __name__ == '__main__':
    main()
    