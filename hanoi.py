#recursion testing

def move(From, To):
    print(f"[*] Moving disk from {From} to {To}")

def hanoi(n,From,HelperPosition,To):
    if n == 0:
        pass
    else: 
        hanoi(n-1,From,To,HelperPosition)
        move(From, To)
        hanoi(n-1 ,HelperPosition,From, To)

hanoi(10,"A","B","C")