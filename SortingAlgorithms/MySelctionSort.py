class MySelectionSort:


    def mysortInPlace(self, data):
        
        for i in range(len(data)-1):
            min_index = i
            print(data)
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            print(data)
            data[i], data[min_index] = data[min_index], data[i]
        return data
        


def main():
    obj = MySelectionSort()
    print(obj.mysortInPlace([3,4,1, 7, 2, 9, 0]))

if __name__ == '__main__':
    main()