def removeDuplicateLetters(s):
    char_map = {}

    for each in s:
        if each in char_map:
            char_map[each] += 1
        else:
            char_map[each] = 1

    print(''.join((sorted(char_map.keys()))))

    #return str(sorted(''.join(char_map.keys())))


print(removeDuplicateLetters('bcabc'))

