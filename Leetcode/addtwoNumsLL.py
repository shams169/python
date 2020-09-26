from linkedList import LinkedList, Node


def add2Sum(l1, l2):
    print('')
    print('inside function...')

    # Declare pointers for traversal. Added for clarity.
    p1 = l1.head
    p2 = l2.head

    # Declare current carry over.
    carry = 0

    # Declare cur variable to help traverse and add nodes to new list.
    # Declare head variable to be the head of the list.
    head = cur = Node(0)

    # Iteration condition.
    while p1 or p2 or carry:

        #print(p1.val, p2.val, carry)

        # Determine current value and carry over.
        sum = carry
        sum += 0 if p1 is None else p1.val
        sum += 0 if p2 is None else p2.val
        if sum >= 10:
            sum -= 10
            carry = 1
        else:
            carry = 0

        print(sum, carry)

        # Add current value as it will always atleast be '1'.
        cur.next = Node(sum)
        cur = cur.next

        # Add base cases for iterating linked lists.
        if p1 is None and p2 is None:
            break
        elif p1 is None:
            p2 = p2.next
        elif p2 is None:
            p1 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next

    print('exiting...')
    print('')

    temp = head.next
    while(temp is not None):
        print(temp.val)
        temp = temp.next


def main():
    
    llist1 = LinkedList()
    llist1.append(Node(2))
    llist1.append(Node(4))
    llist1.append(Node(3))
    #llist1.printNodes()

    llist2 = LinkedList()
    llist2.append(Node(5))
    llist2.append(Node(6))
    llist2.append(Node(4))
    #llist2.printNodes()

    add2Sum(llist1, llist2)



if __name__ == "__main__":
    main()