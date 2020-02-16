def perfect(number):
    total=0
    for i in range(1,number):
        if number%i==0:
            total+=i
    if total==number:
        return (number, 'is a perfect number.')
    else:
        return (number, 'is not a perfect number.')

print(perfect(6))