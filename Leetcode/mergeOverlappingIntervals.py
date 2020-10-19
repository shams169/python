class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def merge_intervals(pairs):
    
    result = [pairs[0]]
    r = 0
    for i in range(1, len(pairs)):
        if result[r].second >= pairs[i].first:
            #print("We have an overlap...")
            newPair = Pair(result[r].first, max(result[r].second, pairs[i].second))
            result[r] = newPair
        else:
            result.append(pairs[i])
            r += 1
    return result


def leetIntervalMerge(intervals):

    result = [intervals[0]]
    r = 0

    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if result[r][1] >= intervals[i][0]:
            newPair = [result[r][0], max(result[r][1], intervals[i][1])]
            result[r] = newPair
        else:
            result.append(intervals[i])
            r += 1

    print(result)


def main():
    v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), 
         Pair(6, 8), Pair(10, 12), Pair(11, 15)]

    # for item in v:
    #     print(item.first, item.second)
    
    # out = merge_intervals(v)

    # for item in out:
    #     print(item.first, item.second)

    leetIntervalMerge([[1,3],[2,6],[8,10],[15,18]])


if __name__ == '__main__':
    main()

    