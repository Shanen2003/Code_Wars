

def create_phone_number(n):
    var = str('')
    var2 = str('')
    var3 = str('')
    for i in range(0,3):
        var += str(n[i])
    first = "(" + var + ") "
    for i in range(3,6):
        var2 += str(n[i])
    second = first + var2 + "-"
    for i in range(6,10):
        var3 += str(n[i])
    final = second + var3
    return final



def create_phone_number(n):
    number = "(" + "".join(map(lambda x: str(x), n[0:3])) + ") " + "".join(map(lambda x: str(x), n[3:6])) + "-" + "".join(map(lambda x: str(x), n[6:10]))
    return number




create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number([0,2,3, 0,0,6,0,0,9,0])