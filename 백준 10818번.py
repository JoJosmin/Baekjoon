N = int(input())
k = list(map(int, input().split()))
maximum = k[0]
minimum = k[0]
for i in k[1:]:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
print(maximum, minimum)


N = int(input())
k = list(map(int, input().split()))

print(min(k), max(k))
