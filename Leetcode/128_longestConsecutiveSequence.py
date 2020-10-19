from collections import Counter
def longestConsecutiveSequence(nums):

    nums_map = Counter(nums)
    print(nums_map)
    longest = 0

    for num in nums:
        count = 1
        if num - 1 in nums_map:
            continue
        curr = num
        while curr+1 in nums_map:
            count += 1
            curr = curr +1

        longest = max(longest, count)
    return longest

print(longestConsecutiveSequence([100,101,102,104, 4, 200, 103, 2, 3, 5]))