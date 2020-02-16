def gcd(x,y):
    result=0
    if x>=y:
        counter=0
        while counter<=y:
            for i in range (1,y+1):
                if x%i==0 and y%i==0:
                    result=i
                    counter+=1
    else:
        counter = 0
        while counter <= x:
            for i in range(1, x + 1):
                if x % i == 0 and y % i == 0:
                    result= i
                    counter += 1
    return result

