#2577번 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
multiply= str(A*B*C)

for i in range(10):
    counting = multiply.count(str(i))
    print(counting)
