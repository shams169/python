from collections import Counter, defaultdict, OrderedDict
import re

def checkAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1_dict = Counter(s1)
        s2_dict = Counter(s2)

        return s1_dict == s2_dict



def recursiveStringReverse(s):
    if len(s) == 0:
        return s
    else:
        return recursiveStringReverse(s[1:])+s[0]


def checkIfOnlyDigits(s):
    match = re.match('(^-)?\d+(\.\d+)?', s)
    if match:
        return True
    else:
        return False
    # for c in s:
    #     if not c.isdigit():
    #         return False
    #     continue
    # return True
    #return s.isnumeric()

#print(recursiveStringReverse("apple"))
#print(recursiveStringReverse("Geeksforgeeks"))


def countVowelsAndConsontants(s):

    count_map = {"vowels": 0, "consonants": 0}
    for c in s:
        if c in "aieou":
            count_map["vowels"] += 1
        else:
            count_map["consonants"] += 1

    return count_map


def findAllPermutations(s, step =0):
    if step == len(s):
        print(''.join(s))
    
    for i in range(step, len(s)):
        str_copy = [c for c in s]
        print(str_copy)
        str_copy[step], str_copy[i] = str_copy[i], str_copy[step]
        findAllPermutations(str_copy, step+1)


def printDuplicateChars(S):

    out = Counter(S)
    for i in out:
        if out[i] > 1:
            print('Duplicate: {}'.format(i))

def checkAnagram2(S1, S2):

    is_anagram = False
    if len(S1) != len(S2):
        is_anagram =  False
    elif sorted(S1) != sorted(S2):
        is_anagram = False
    is_anagram = True

    if is_anagram:
        return f"{S1} and {S2} are anagrams"
    else:
        return f"{S1} and {S2} are not anagrams"




def recursiveStringReverse2(s, result=[]):
    if len(s) == 0:
        return s
    else:
        return recursiveStringReverse2(s[1:])+s[0]


def firstNonRepeatedChar(s):

    char_map = OrderedDict()

    for c in s:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1


    print(char_map)
    for i in char_map:
        if char_map[i] == 1:
            return i
            break

def atoi(s):
    INT_MAX = 2**31 -1
    INT_MIN = -2**31
    out = ""
    sign = ""
    count = 0
    for c in s:
        if c == " ":
            continue
        if (c not in ['+', '-']) and (c.isdigit()== False) and count == 0:
            return 0
        if c in ['+', '-']:
            sign = c
            count += 1
        elif c.isdigit():
            out += str(c)
            count += 1
        elif count > 0 and c.isdigit() == False:
            break
        else:
            continue
        
    if out == "":
        return 0
    elif sign:
        out = sign + out
    else:
        out = int(out)
    
    if int(out) > INT_MAX:
        return INT_MAX
    elif int(out) < INT_MIN:
        return INT_MIN
    else:
        return int(out)

    # for c in s:
    #     if c.isdigit():
    #         continue
    #     else:
    #         return(f'{s} is not an integer string')
    # return int(s)


def reverseWordsInSentence(sen):
    return ' '.join(sen.split()[::-1])


def checkStringRotation(s1, s2):

    if len(s1) != len(s2):
        return f"{s1} and {s2} are  of different lengths and cannot be rotations of each other"
    s = s1 + s1
    print(s)

    if s2 in s:
        return f"{s1} and {s2} are rotations of each other"
    else:
        return f"{s1} and {s2} are not rotations of each other"


def lenLongestSubWithNonRepeatChars(A):

    sub_start_index = 0
    longest_sub = ""
    longest_len = 0
    out = []
    sub_map = {}

    for i in range(0,len(A)):

        if A[i] in sub_map and sub_start_index <= sub_map[A[i]]:
            sub_start_index = sub_map[A[i]]
            out.append(A[sub_start_index:i])
        else:
            longest_len = max(longest_len, i - sub_start_index +1)
            out.append(A[sub_start_index:i+1])
            
        sub_map[A[i]] = i
            # out.append(temp)
            # if len(temp) > len(longest_sub):
            #     longest_sub = temp
            #     longest_len = len(temp)
            # sub_start_index += 1
        
    #     sub_map[A[i]] = i
    print(out)
    return longest_len


def longestPalindromicSubstr(s):

    def helper(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    res = ""
    for i in range(len(s)):
        test = helper(i, i)
        if len(test) > len(res):
            res = test
        
        test = helper(i, i+1)
        if len(test) > len(res):
            res = test
    return res

def longestCommonPrefix(A):

    lcp = ""
    i = 0
    while i < len(A[0]):
        c = A[0][i]

        for j in range(1, len(A)):
            if A[j][i] != c:
                return lcp
        
        lcp += c
        i += 1
    return lcp



    

#print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","dogger"]))

#print(lenLongestSubWithNonRepeatChars('abcabcab'))
#print(longestPalindromicSubstr('babad'))

#print(checkStringRotation('IndiaUSAEngland', 'USAnglandIndia'))

#print(reverseWordsInSentence("Hello from python"))
#print(printDuplicateChars('Programming'))
#print(checkAnagram2('listen', 'silent'))
#print(findAllPermutations("one"))  
#print(recursiveStringReverse2("Hello"))
#print(firstNonRepeatedChar('geekforgeeks'))
#print(atoi('123a4'))
# input_vals = ["123", "-123" , "123.12", "abcd123"]
# for i in input_vals:
#     print(checkIfOnlyDigits(i))

#print(countVowelsAndConsontants('aeiou'))

#print(checkAnagram('word', 'wrdo'))