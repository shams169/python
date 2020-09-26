class Solution:
    def threeSum(self, nums, target):

        result = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i >0 and nums[i] == nums[i-1]: continue

            while(left < right):
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]: 
                        right -= 1
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
        return result




def main():
    obj = Solution()
    print(obj.threeSum([-1,0,1,2,-1,-4], 0))

if __name__ == '__main__':
    main()