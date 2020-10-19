import random

class Solution():
    def findMissingNumber(self,nums):
        n = len(nums)



        for i in range(len(nums)-1):
            if nums[i+1] != nums[i] + 1:
                return nums[i]+1

    def hashingSolution(self, nums):
        nums_set = set()

        for i in nums:
            nums_set.add(i)
        print(nums_set)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
        return -1

    def nSumSolution(self, nums):
        n = len(nums)
        nSum = int(n*(n+1)/2)
        print(nSum)
        total = 0
        for i in nums:
            total += i
        
        diff = int(nSum - total)
        if diff == 0:
            return -1
        else:
            return diff



def main():
    obj = Solution()
    nums = [3,0,1]
    #print(obj.findMissingNumber(nums))

    nums = [i for i in range(50)]
    pop_index = random.randint(0,50)
    nums.pop(pop_index)

    print(pop_index)
    random.shuffle(nums)
    #print(obj.hashingSolution(nums))
    print(obj.nSumSolution(nums))


if __name__ == '__main__':
    main()
