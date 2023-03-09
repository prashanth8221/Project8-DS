#stack implementation using list
stack=[]
def push():
    element=int(input('enter the elemnt: '))
    stack.append(element)
    print(stack)
def pop_ele():
    if not stack:
        print('stack is empty')
    else:
        e=stack.pop()
        print('removed element: ',e)
        print(stack)
while True:
    print("choose the operation 1.push 2.pop 3.quit")
    choose=int(input(''))
    if choose==1:
        push()
    elif choose==2:
        pop_ele()
    elif choose==3:
        break
    else:
        print('choose the correct operation')
