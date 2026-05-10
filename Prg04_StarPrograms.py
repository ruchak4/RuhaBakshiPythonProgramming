
#   This is a Sqaure Grid Program

row_num = int(input("Pls enter grid row number: "))
col_num = int(input("Pls enter grid column number: "))

def grid():
    for row in range(row_num):
        for col in range(col_num):
            print('*', end=" ")
        print()
    
grid()    