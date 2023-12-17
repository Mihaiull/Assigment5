
#Global sorting function:
def srt(whatever, key = None, reverse = False):
    if key == None:
        key = lambda x: x
    if type(whatever) != list:
        raise ValueError("The argument must be a list")
    if type(reverse) != bool:
        raise ValueError("The reverse argument must be a boolean")
    if reverse:
        for i in range(len(whatever)):
            for j in range(len(whatever)):
                if key(whatever[i]) > key(whatever[j]):
                    whatever[i], whatever[j] = whatever[j], whatever[i]
    else:
        for i in range(len(whatever)):
            for j in range(len(whatever)):
                if key(whatever[i]) < key(whatever[j]):
                    whatever[i], whatever[j] = whatever[j], whatever[i]
    return whatever

#Global filtering function:
def flt(whatever, key = None):
    if key == None:
        key = lambda x: x
    if type(whatever) != list:
        return ValueError("The argument must be a list")
    for i in range(len(whatever)-1, -1, -1):
        if not key(whatever[i]):
            whatever.pop(i)
    return whatever

#Global searching function:
def srch(whatever, key = None):
    if key == None:
        key = lambda x: x
    if type(whatever) != list:
        return ValueError("The argument must be a list")
    searched = []
    for i in range(len(whatever)):
        if key(whatever[i]):
            searched.append(whatever[i])
    if len(searched) > 0:
        return searched
    return None

if __name__ == "__main__":
    print("This module is not meant to be run by itself!")
    #a few tests:
    testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(srt(testList, reverse=True))
    print(srt(testList, key=lambda x: x % 2 == 0))
    print(flt(testList, key=lambda x: x % 2 == 0))
    print(srch(testList, key=lambda x: x % 4 == 0))
    #hide other keys pressed in the terminal:
    input("Press any key to exit...")
    exit()