from stack import Stack


def checkBalancedParans(expr):
    open_parans = ['(', '[', '{']
    close_parans = [')', ']', '}']
    parans_pair = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    
    charStack = Stack()

    for c in expr:
        if c in open_parans:
            charStack.push(c)
            continue
        elif c in close_parans:
            topElement = charStack.getTop()
            if parans_pair[topElement] == c:
                charStack.pop()
            else:
                return False
        else:
            print("Invalid Char: {}".format(c))
            return False
    
    if charStack.isempty():
        return True
    return False







def main():
    print(checkBalancedParans('[()]'))

if __name__ == "__main__":
    main()