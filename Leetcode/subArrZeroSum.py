def subArrayZeroSum(nums):
    pass


# Utility function to insert <key, value> into the dict
def insert(dict, key, value):

	# if the key is seen for the first time, initialize the list
	dict.setdefault(key, []).append(value)


# Function to print all sub-lists with 0 sum present
# in the given list
def printallSublists(A):

	# create an empty -dict to store ending index of all
	# sub-lists having same sum
	dict = {}

	# insert (0, -1) pair into the dict to handle the case when
	# sub-list with 0 sum starts from index 0
	insert(dict, 0, -1)

	sum = 0

	# traverse the given list
	for i in range(len(A)):

		# sum of elements so far
		sum += A[i]

		# if sum is seen before, there exists at-least one
		# sub-list with 0 sum
		if sum in dict:

			list = dict.get(sum)

			# find all sub-lists with same sum
			for value in list:
				print("Sublist is", (value + 1, i))

		# insert (sum so far, current index) pair into the -dict
		insert(dict, sum, i)


from collections import defaultdict
def printSubList(A, target):

    sdict = {}
    sdict.setdefault(0, []).append(-1)
    result = []
    curr_sum = 0

    for index in range(len(A)):
        curr_sum += A[index]
        print('Current Sum: {}'.format(curr_sum))

        diff = curr_sum - target
    
        print('Diff: {}'.format(diff))
        if diff in sdict:
            subArrayList = sdict.get(diff)
            print('SubArray for diff: {} = {}'.format(diff, subArrayList))
            for value in subArrayList:
                result.append(A[value+1:index+1])
        
        sdict.setdefault(curr_sum, []).append(index)
    
    print(result)


def main():
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    #print(subArrayZeroSum([4, 2, -3, -1, 0, 4]))
    #printallSublists(A)
    printSubList(A, 7)

if __name__ == '__main__':
    main()