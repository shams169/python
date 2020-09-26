def checkIfPalindrome(s):

    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    
    odd_count = 0
    for key, value in char_count.items():
        if value%2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
        
    return True
    
def canFormPalindrome(strr): 
      
    # Create a listt 
    listt = [] 
      
    # For each character in input strrings, 
    # remove character if listt contains 
    # else add character to listt 
    for i in range(len(strr)): 
        if (strr[i] in listt): 
            listt.remove(strr[i]) 
        else: 
            listt.append(strr[i]) 
              
    # if character length is even listt is expected to be empty 
    # or if character length is odd listt size is expected to be 1 
    if (len(strr)% 2 == 0 and len(listt) == 0 or \
        (len(strr) % 2 == 1 and len(listt) == 1)): 
        return True
    else: 
        return False
  
# Driver code 
if (canFormPalindrome("geeksforgeeks")): 
    print("Yes") 
else: 
    print("No") 
      
if (canFormPalindrome("geeksogeeks")): 
    print("Yes") 
else: 
    print("No") 

print(checkIfPalindrome('geeksforgeeks'))
print(checkIfPalindrome('torro'))
print(checkIfPalindrome('mmo'))
print(checkIfPalindrome('ssssss'))


