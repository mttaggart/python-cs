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

print(pal_iter("racecar"))
