def sqrt_recur(num,test):
    epsilon = 0.01
    #Like any good recursion, we need a base case.
    if abs((test*test)-num) <= epsilon:
        return test
    else:
    #And here's where we do our bisection, calling sqrt_recur either way
        if test*test > num:
            return sqrt_recur(num,test/2.0)
        else:
            return sqrt_recur(num,(test+test*2.0)/2.0)

print(sqrt_recur(25,25/2.0))
