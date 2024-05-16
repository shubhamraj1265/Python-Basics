# print reverse table using for loop

def reverse_multiplication(n):
    Table = 0
    for i in range(10, 0, -1):
        Table = n * i
        print(Table)
        
reverse_multiplication(4)
