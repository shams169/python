#!/usr/bin/env python3

class Solution(object):
    def longestCommonPrefix(self, input):
        current = ''
        prefix = ''

        if len(input) == 0:
            return prefix

        for i in range(len(input[0])):
            for j, val in enumerate(input):
                try:
                    if j == 0:
                        current = val[i]
                    elif val[i] != current:
                        return prefix
                    else:
                        pass
                except IndexError:
                    return prefix
            prefix += current
        
        return prefix
    
    def faster(self, input):
        if not input:
            return ""

        s1 = min(input)
        s2 = max(input)
        print(s1, s2)
        
        for i, c in enumerate(s1):
            print(i,c)
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1


    #def oneLiner(self, input):
    #    return "".join(map(itemgetter(0), takewhile(lambda x: len(set(x))==1, zip(*strs))))


def main():
    #input = ["flower","flow","flight"]
    input = ["dog","racecar","car"]
    obj = Solution()
    
    #print(obj.longestCommonPrefix(input))
    print(obj.faster(input))

 
if __name__ == '__main__':
    main()