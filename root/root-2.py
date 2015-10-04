def sqrt(num):
    epsilon = 0.01
    guesses = 0
    test = num/2.0
    while abs((test*test)-num) > epsilon:
        print("Guessing {}".format(test))
        if test*test > num:
            test /= 2.0
        else:
            test = (test + (test*2.0)) / 2.0
        guesses += 1
    print("Total guesses: {}".format(guesses))
    return test

print(sqrt(25))
