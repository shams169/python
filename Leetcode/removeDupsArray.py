def removeDuplicates(nums):

    # Super simple solution 
    # mp = {i : 0 for i in nums}
    # print(list(mp.keys()))

    nmap = {}
    ans = []
    for n in nums:
        if n not in nmap:
            nmap[n] = 0
            ans.append(n)

    print(ans)
        
def removeDupsSorted(nums):

    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            #del nums[i]
            nums.pop(i)
    print(nums)


#removeDuplicates([ 1, 2, 5, 1, 7, 2, 4, 2 ])
removeDupsSorted([1,1,1,3,4,5,5,5,5,7,7,7,9,9])