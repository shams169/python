#!/usr/bin/env python3

class Solution:

    # This is a brute force solution 
    def longestSubstr(self, S):
        out = []
        longest = 0
        
        for i in range(0,len(S)):
            k = i+1
            while(k <= len(S)):
                #print(i,k)
                out.append(S[i:k])
                k += 1
        for item in out:
            #print(set(item), len(item))
            if len(set(item)) == len(item) and longest <= len(item):
                longest = len(item)
                #print('XXX Longest: {}'.format(longest))


        print(out)
        print(longest)
        
    # Sliding window technique

    def longestNonRepeatSubStr(self, S):

        max_len = 0
        char_dict = {}
        start = 0

        if len(S) == 0 :
            return 0

        for i in range(len(S)):
            if S[i] in char_dict and start <= char_dict[S[i]]:
                start = char_dict[S[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            char_dict[S[i]] = i
            print(start, max_len)
            print(char_dict)
        
        print(max_len)
        return max_len


def main():
    obj = Solution()
    obj.longestNonRepeatSubStr('abcabcbbefgh')


if __name__ == "__main__":
    main()