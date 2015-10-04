def sqrt(num):
    test = num/2.0
    while test * test != num:
        print("Guessing {}".format(test))
        if test*test > num:
            test /= 2.0
        else:
            test = (test + (test*2.0)) / 2.0
    return test

print(sqrt(16))
