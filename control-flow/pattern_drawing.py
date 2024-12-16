size = int(input("Enter the size of the pattern: "))

i = 0
while i < size:
    for _ in range(size):
        print("*", end="")
    print()
    i += 1
