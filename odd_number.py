# Print the odd number using for loop

def odd_number(n):
    for i in range(1, n+1, 1):
        if(i % 2 != 0):
            print(i)
        
odd_number(20)

# Print the odd nuber using while loop

def odd_number(n):
    i = 1
    while(i <= n):
        if(i % 2 != 0):
            print(i)
        i += 1
        
odd_number(30)
