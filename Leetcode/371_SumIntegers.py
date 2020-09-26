#!/usr/bin/env python3

def sumInts(a, b):
    
      total = a ^ b
      carry = a & b
      
      if carry == 0:
          return total
      else:
          carry = carry << 1
          return sumInts(total, carry)

def CorrectSolution(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)


def main():
    #print(sumInts(-1,1))
    print(CorrectSolution(-1,1))

if __name__ == '__main__':
    main()