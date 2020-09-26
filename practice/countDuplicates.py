def countDups(nums):
    out = {}

    for i in nums:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    
    count = 0
    for  value in out.values():
        if value > 1:
            count += 1
    return count
        


def main():
    nums = [1, 1, 2, 3, 3, 4, 5, 5, -1, -1]

    print(countDups(nums))

if __name__ == '__main__':
    main()