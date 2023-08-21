queue = []

def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(element, "is added to the queue!")

def dequeue():
    if not queue:
        print("Queue is Empty!!")
    else:
        e=queue.pop(0)
        print("Element removed!",e)

def display():
    print(queue)

while True:

    print("QUEUE IMPLEMENTATION PROGRAM!")
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Display')

    print('5. Exit')
    ch = int(input("Enter the choice(1-5)"))
    if ch == 1:
        enqueue()

    elif ch == 2:
        dequeue()

    elif ch == 3:
        display()

    elif ch == 5:
        break
    else:
        print("Please choose the right option")