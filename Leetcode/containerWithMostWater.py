#!/usr/bin/env python3


def maxArea(height):
    i = 0
    j = len(height) - 1
    max_area=0

    while(i < j):
        area = (j-i) * min(height[i], height[j])
        max_area = max(area, max_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    print(max_area)


maxArea([1,8,6,2,5, 4, 8,3,7])