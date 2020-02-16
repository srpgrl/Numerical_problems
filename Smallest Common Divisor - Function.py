def scd(x, y):
    counter = 1
    if x == y:
        return x

    elif x > y:
        result = x * counter
        while ((result) % y) != 0:
            counter += 1
            result = x * counter
    else:
        result = y * counter
        while result % x != 0:
            counter += 1
            result = y * counter

    return result



print(scd(6,1))
print(scd(22,15))
print(scd(21,15))
