class Solution:
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        print(nums)
        closestSum = sum(nums[:3])


        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while(left < right):
                currSum = nums[i] + nums[left] + nums[right]
                print(abs(currSum - target), abs(closestSum - target))
                if abs(currSum - target) < abs(closestSum - target):
                    closestSum = currSum
                if currSum < target:
                    left += 1
                else:
                    right -= 1

        return closestSum




def main():
    obj = Solution()
    print(obj.threeSumClosest([-1, 2, 1, -4], 1))

if __name__ == '__main__':
    main()