x = int(input())
y = int(input())

if x >= -1000 and x < 0:
    if y >= -1000 and y < 0:
        print('3')
    else:
        print('2')

if x >0 and x <= 1000:
    if y >= -1000 and y < 0:
        print('4')
    else:
        print('1')
