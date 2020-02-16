print(""" Helloooo

**********************
Factorial Finding Program
**********************

Press Q for quit. 
**********************""")

while True:
    num=(input('Enter the number whose factorial you want to find: '))
    if num=='Q':
        break

    else:
        num=int(num)
        factorial=1
        for i in range(2,num+1):
            factorial *= i
        print("Factoral of {} is {}".format(num,factorial))