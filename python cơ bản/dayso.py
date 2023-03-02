def isAlt(a):
    for i in range(0, len(a)-1):
        if a[i]*a[i+1] < 0:
            return True

    return False
def isGrow(a):
    for i in range(0, len(a) -1):
        if a[i] > a[i+1]:
            return False
    return True
def isMulti(a):
    for i in range(0, len(a)-2):
        if a[i+1]/a[i] != a[i+2]/a[i+1]:
            return False
    return True
def isAdd(a):
    for i in range(0, len(a)-2):
        if a[i+2] + a[i] == 2*a[i+1]:
            return True
    return False
print(isAdd([1,2,3,4,5,6,7]))