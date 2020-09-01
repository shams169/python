#!/usr/bin/env python3

class Solution(object):
    def romanToInt(self, input):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        
        output = 0
        while(i < len(input)):
            #print(input[i])
            if input[i] not in roman.keys():
                return ("Not a valid roman input")

            if (i+1 < len(input)) and (input[i]+input[i+1] in roman.keys()):
                output += roman[input[i]+input[i+1]]
                #print(output)
                i += 2
            else:
                output += roman[input[i]]
                #print(output)
                i += 1
        return output



def main():
    obj = Solution()
    print(obj.romanToInt('MCMXCIV'))
 
if __name__ == '__main__':
    main()




