chars = ["*", "."]
cases = int(input())
for k in range(cases):
    line = input()
    l, c = [int(y) for y in line.split()]
    for i in range(l):
        for j in range(c):
            print("{}".format(chars[(i+j) % 2]), end="")
        print()
    print()
