
def prime (number):
    if number == 1:
        return False
    elif number ==2:
        return True
    else:
        for i in (2,number):
            if number%i==0:
                return False
            return True

while True:
    num=input('Please enter a number or enter q for quit: ')

    if num== 'q':
        break
    else:
        num=int(num)

        if prime(num)== True :
            print(num, 'is a prime number')
        else:
            print(num,'is not a prime number')
