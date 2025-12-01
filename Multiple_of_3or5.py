
def solution(number):
    i = 0
    i2 = 0
    l = []
    l2 = []
    l3 = []
    final = 0
    while i < number:
        l.append(i)
        i += 3
    while i2 < number:
        l2.append(i2)
        i2 += 5
    l3 = [x for x in l2 if x % 3 !=0]
    final = sum(l) + sum(l3)
    return final

def solution(number):
    l3 = list(range(0, number, 3))         
    l5 = [x for x in range(0, number, 5)    
          if x % 3 != 0]                    
    return sum(l3) + sum(l5)

def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

solution(16)