class Solution:
    def fourSum(self, nums, target):

        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]: continue

            j = i+1

            while(j <= len(nums)-3):
                k = j+1
                r = len(nums) -1

                while(k < r):
                    temp = nums[i] + nums[j] + nums[k] + nums[r]

                    if temp == target:
                        result.append((nums[i], nums[j], nums[k], nums[r]))
                        k_val = nums[k]
                        while(k < len(nums) and nums[k] == k_val):
                            k += 1
                        
                        r_val = nums[r]
                        while(r > k and nums[r] == r_val):
                            r -= 1
                        
                        k += 1
                        r -= 1
                    elif temp < target:
                        k += 1
                    else:
                        r -= 1
                j += 1
        return result
      




def main():
    obj = Solution()
    #print(obj.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(obj.fourSum([0,0,0,0], 0))


if __name__ == '__main__':
    main()

