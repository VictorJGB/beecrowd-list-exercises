while True:
    try:
        A = int(input())
        if(A % 6 == 0): 
            print("Y")
        else:
            print("N")
        
    except EOFError:
        break