#!/usr/bin/env python3


class Solution:
    
    
  
    def myAtoi(self, s):
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        out = ""
        white_check = False
        sign = None
        for c in s:
            if not white_check and c == ' ':
                continue
            elif c in ['+', '-'] and sign is None:
                sign = c
                white_check = True
            elif not c.isdigit():
                break
            else:
                out += c
            
            
            
        if len(out) == 0:
            return 0
        elif sign is not None:
            out = sign + out
        
        out = int(out)

        if out > INT_MAX:
            return INT_MAX
        elif out < INT_MIN:
            return INT_MIN
        else:
            return out




def main():
    obj = Solution()
    print(obj.myAtoi("-"))


if __name__ == "__main__":
    main()
