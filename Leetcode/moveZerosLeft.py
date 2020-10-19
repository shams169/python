def moveZerosLeft(nums):

    # found_index = 0
    # j = 0
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         found_index = i

    #         for k in range(found_index, j, -1):
    #             nums[k] = nums[k-1]
    #         nums[j] = 0
    #         j += 1
            
    
    # print(nums)


    r = len(nums) - 1
    w = len(nums) - 1

    while(r >= 0):
        if nums[r] != 0:
            nums[w] = nums[r]
            w -= 1
        r -= 1
    
    while(w >= 0):
        nums[w] = 0
        w -= 1
    print(nums)

def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  while(read_index >= 0):
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1

    read_index -= 1

  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1

#v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
v = [1, 10, 20, 78, 59, 63, 47, 88, 98]
print("Original Array:", v)

#move_zeros_to_left(v)
moveZerosLeft(v)

print("After Moving Zeroes to Left: ", v)



#moveZerosLeft([1, 10, 20, 0, 59, 63, 0, 88, 0])

