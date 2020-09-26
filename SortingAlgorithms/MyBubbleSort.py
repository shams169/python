class MyBubbleSort:


    def myBubbleSort(self, data):
        
        for i in range(len(data)):
            for j in range(len(data) -1 ):
                if data[j+1] < data[j]:
                    data[j+1], data[j] = data[j], data[j+1]
            print(data)
        return data        


def main():
    obj = MyBubbleSort()
    print(obj.myBubbleSort([3,4,1, 7, 2, 9, 0]))

if __name__ == '__main__':
    main()