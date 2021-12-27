chars = ["*", "."]
n = int(input())
for k in range(n):
    x = input()
    l, c = [int(y) for y in x.split()]
    for i in range(l):
        for j in range(c):
            print("{}".format(chars[(i+j) % 2]), end=" ")
        print()
    print()
