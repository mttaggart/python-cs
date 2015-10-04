import time

def pal_recur(test):
    print(test)
    if len(test) == 1:
        return True
    elif len(test) == 2:
        return test[0] == test[-1]
    else:
        if test[0] == test[-1]:
            return pal_recur(test[1:-1])
        else:
            return False

def pal_iter(test):
    while len(test) > 0:
        print(test)
        if len(test) == 1:
            return True
        elif len(test) == 2:
            if test[0] == test[-1]:
                return True
            return False
        else:
            if test[0] == test[-1]:
                test = test[1:-1]
            else:
                return False

def time_test(func, func_name, func_arg):
    start = time.time()
    result = func(func_arg)
    end = time.time()
    print("Result: {}".format(result))
    print("Execution of {} took {} ms".format(func_name,(end-start)))


time_test(pal_iter, "Iterative", "racecar")
time_test(pal_recur, "Recursive", "racecar")
