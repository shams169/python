class MyInsertionSort:


    def myInsertionSort(self, data):
        for i in range(1, len(data)):
            hole = i
            value = data[i]

            while(hole > 0 and data[hole-1] > value):
                data[hole] = data[hole -1 ]
                hole -= 1
            data[hole] = value
            print(data)
        
        return data
        


def main():
    obj = MyInsertionSort()
    print(obj.myInsertionSort([3,4,1, 7, 2, 9, 0]))

if __name__ == '__main__':
    main()