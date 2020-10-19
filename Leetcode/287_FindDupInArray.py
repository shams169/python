class Solution:
    def findDuplicate(self, nums):
        nums_map = {}

        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1
        
        for key, value in nums_map.items():
            if value > 1:
                return key
        return None

    def floydSolution(self, nums):
        """
        This solution is based on the floyds algorithm which is used to identify the circular property of a linkedlist 
        kind of data structure.
        This is one good explanation for the algorithm: (https://medium.com/@tuvo1106/the-tortoise-and-the-hare-floyds-algorithm-87badf5f7d41)
        Also this youtube video: https://www.youtube.com/results?search_query=leetcode+find+the+duplicate+number+python
        
        """
        print(nums)
        turtle = hare = nums[0]

        turtle = nums[turtle]
        hare = nums[nums[hare]]
        print(turtle, hare)

        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
            print(turtle, hare)

        turtle = nums[0]
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]

        return turtle




def main():
    obj = Solution()
    #print(obj.findDuplicate([1,2,2,3,4,5]))
    print(obj.floydSolution([1,2,3,3,4,5]))


if __name__ == '__main__':
    main()