def kbc(n,c):

    if n > 0 and n < 5: 
        if n == c: 
            print("\nCongratulation\n")
        else: 
            print("\nYou May Leave Here!\n")
    else:
        print("\nInvalid Input\n")

    return 0;   


print("Q.no:1.  What which is the largest river in the world?")

l = ['Bagmati', 'Amazon', 'Nile', 'Yamuna',]
for i in range(4):
    print(str(i+1)+". "+str(l[i]))

inp = int(input("Enter the number of Option: "))

kbc(inp,2)
