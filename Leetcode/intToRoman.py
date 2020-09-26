#!/usr/bin/env python3


class Solution:
    def intToRoman(self, num):
        roman_dict = { 1 : 'I',
                       5: 'V',
                       10: 'X', 
                       50: 'L', 
                       100: 'C', 
                       500: 'D', 
                       1000: 'M', 
                       4: 'IV', 
                       9: 'IX', 
                       40: 'XL', 
                       90: 'XC', 
                       400: 'CD' , 
                       900:'CM' }
        out = ''
        while(num > 0):
            if num >= 1000:
                out += roman_dict[1000]
                num -= 1000
            elif num >= 900:
                out += roman_dict[900]
                num -= 900
            elif num >= 500:
                out += roman_dict[500]
                num -= 500
            elif num >= 400:
                out += roman_dict[400]
                num -= 400
            elif num >= 100:
                out += roman_dict[100]
                num -= 100
            elif num >= 90:
                out += roman_dict[90]
                num -= 90
            elif num >= 40:
                out += roman_dict[40]
                num -= 40
            elif num >= 50:
                out += roman_dict[50]
                num -= 50
            elif num >= 10:
                out += roman_dict[10]
                num -= 10
            elif num >= 9:
                out += roman_dict[9]
                num -= 9
            elif num >= 5:
                out += roman_dict[5]
                num -= 5
            elif num >= 4:
                out += roman_dict[4]
                num -= 4
            elif num >= 1:
                out += roman_dict[1]
                num -= 1
        
        return out
    
    def optimized(self, nums):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


        result = ''

        for i in range(0, len(values)):
            while(nums >= values[i]):
                result += numerals[i]
                nums -= values[i]

        return result

def main():
    obj = Solution()
    print(obj.optimized(1994))


if __name__ == '__main__':
    main()




