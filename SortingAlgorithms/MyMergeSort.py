class MyMergeSort:

    def myMergeSort(self, data):
        
        if len(data) < 2:
            return
        
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        self.myMergeSort(left)
        self.myMergeSort(right)
        self.merge(left, right, data)
        return data
        

    def merge(self, left, right, data):
        
        i = 0
        j = 0
        k = 0
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                data[k] = left[i]
                k += 1
                i += 1
            else:
                data[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1 
        
        


def main():
    obj = MyMergeSort()
    print(obj.myMergeSort([3,4,1, 7, 2, 9, 0]))

if __name__ == '__main__':
    main()