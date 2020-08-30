#!/usr/bin/env python3

# Youtube video which explains the algorithm
# https://www.youtube.com/watch?v=GuTPwotSdYw


def permutate(a, l, r):
    if l == r:
        print(''.join(a))

    for i in range(l, r+1):
        a[l], a[i] = a[i], a[l]
        permutate(a, l+1, r) 
        a[l], a[i] = a[i], a[l]


a = 'ABCD'
permutate(list(a), 0, len(a)-1)
