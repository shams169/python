def flightBookings(data):
    output = {}
    result = []

    for item in data:
        print(item)
        start_index, end_index, bookings = item[0], item[1], item[2]

        for i in range(start_index, end_index+1):
            if i in output:
                output[i] += bookings
            else:
                output[i] = bookings
    
    for key in sorted(output.keys()):
        result.append(output[key])
    return result
    

0

def main():
    print(flightBookings([[1,2,10], [2,3,20],[2,5,25]]))


if __name__ == '__main__':
    main()