A = int(input())
B = input()

listB = []
for k in list(B):
    k = int(k)
    listB.append(k)
listB.reverse()    
result = 0
for b, i in zip(listB, [1, 10, 100]):
    b = int(b)
    print(A*b)
    result+= A*i*b

print(result)

