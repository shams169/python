def countValleys(steps):

    sea_level = 0
    valley_count = 0
    for step in steps:
        print(step)
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valley_count += 1
        else:
            sea_level -= 1
        
    
    return valley_count


def main():
    steps = list('UDDDUDUU')
    print(countValleys(steps))

if __name__ == '__main__':
    main()
