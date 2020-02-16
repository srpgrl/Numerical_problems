
units_digit  = ['','one','two','three','four','five','six','seven','eight','nine']
tens_digit = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

def reading(number):
    unit= (int((str(number))[1]))
    tens = (int((str(number))[0]))
    return tens_digit[tens] , units_digit[unit]

print(reading(46))

