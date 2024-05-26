def check(n):
    if(n > 0):
        print("Positive Number")
    elif(n < 0):
        print("Negative Number")
    else:
        print("Null Number")

a = int(input("Enter any Number: "))
check(a)