def make():
    N = int(input())
    for i in range(1, 1000001):
        k = 0

        for j in str(i):
            j = int(j)
            k += j+i
        if k == N:
            return i

a = make()
if a == None:
    print("0")

else:
    print(a)
        
