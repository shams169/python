def find_left(nums, left, right, target):
    while(left < right):
        mid = (left+right)//2

        if nums[mid] < target:
            left = mid+1
        elif nums[mid-1] < target:
            return mid
        else:
            right = mid -1
    return left


def find_right(nums, left, right, target):
    
    while(left < right):
        mid = (left+right)//2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid+1] > target:
            return mid
        else:
            left = mid + 1
    return right



def searchRange(nums, target):
    left = 0
    right = len(nums) -1
    found = False

    while(left <= right):
        mid = (left+right) // 2

        if nums[mid] == target:
            found = True
            break
        
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid + 1

    if not found:
        return [-1, -1]

    return [find_left(nums, 0, mid, target), find_right(nums, mid, len(nums)-1, target)]



#print(searchRange([5,7,7,8,8,10], 10))
print(searchRange([2,2], 2))
#print(searchRange([1], 1))