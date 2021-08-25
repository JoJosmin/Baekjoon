def IsLeapYear(year):

    if year % 4 == 0: 
        
        if year % 100 ==0 : 
            
            if year%400 ==0 :  
                print("1")
            
            else: 
                print("0")
            
        else:
            print("1")
        
    else: 
        print("0")

while True:
    inputyear = int(input())
    if inputyear >0:
        if IsLeapYear(inputyear):
            print("%d년은 윤년입니다," %inputyear) 

        else:
            print("%d년은 윤년이 아닙니다." %inputyear) 
   
