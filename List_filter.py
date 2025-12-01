def filter_list(l):
    l2 = []
    for i in l: 
        if isinstance(i, (int, float)):
            l2.append(i)
        else:        
            pass
    return l2

filter_list([2,3,'str', 6, 'k'])