def square_digits(num):
    var = str(num)
    var3 = str("")
    l = []
    for i in var:
        var = int(i)
        var2 = var * var
        l.append(str(var2))
    final = "".join(l)
    return int(final)


square_digits(765)