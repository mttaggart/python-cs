def pal_recur(test):
    if len(test) == 1:
        return True
    elif len(test) == 2:
        return test[0] == test[-1]
    else:
        if test[0] == test[-1]:
            return pal_recur(test[1:-1])
        else:
            return False

print(pal_recur("abba"))
