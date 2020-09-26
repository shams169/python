class Solution:
    
    def swap(self, x,y):
        x = x + y
        y = x - y
        x = x - y
        return (x,y)


def main():
    obj = Solution()
    out = obj.swap(4,2)
    print(out)


if __name__ == '__main__':
    main()