
x = int(input("input number of rows: "))
y = 1
for row in range(1, x+1):
    for col in range(1, row+1):
        print(y, end="")
        y=y+1
    print()