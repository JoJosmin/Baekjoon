H, M = map(int, input().split())

if M > 45 and M < 60:
    if H >= 0 and H <= 23:
        print(H, end = ' ')
        print(M-45)


elif M <= 45 and M >= 0:
    if H == 0:
        
        if M == 45:
            print('0', end = ' ')
            print('0')
        else:
            print('23', end = ' ')
            print(M+15)
    elif H > 0 and H <= 23:
        print(H-1, end = ' ')
        if M == 45:
            print('0')
        else:
            print(M+15)
