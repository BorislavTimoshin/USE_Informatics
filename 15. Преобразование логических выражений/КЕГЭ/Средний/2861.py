from math import ceil

P = range(69, 92)
Q = range(77, 115)
lst = []
numbers = [0.5 * i for i in range(300)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 69 <= x <= 91
                qq = 77 <= x <= 114
                aa = a1 <= x <= a2
                f = qq <= ((pp == qq) or ((not pp) <= aa))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
