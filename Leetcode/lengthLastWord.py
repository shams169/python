"""
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

class Solution:
    def lengthOfLastWord(self, s):

        words = s.split(' ')
        print(words)

        word  = [w for w in words if w != '']

        if len(word) == 0:
            return 0
        else:
            word = words[-1]
            return len(word)



def main():
    obj = Solution()
    print(obj.lengthOfLastWord(''))


if __name__ == '__main__':
    main()