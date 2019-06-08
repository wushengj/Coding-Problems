datelist = input().split('/')
y = int(datelist[0])
m = int(datelist[1])
d = int(datelist[2])

a = [1,3,5,7,8,10,12] #31 days
b = [4,6,9,11] #30 days

def f_r(mm, dd):
    n = 1
    day_mm = 0
    while n < mm:
        if n in a:
            day_mm = day_mm + 31
        elif n in b:
            day_mm = day_mm + 30
        else:
            day_mm = day_mm + 29
        n = n+1
    else:
        num = day_mm + dd
    return num

def f_n(mm, dd):
    n = 1
    day_mm = 0
    while n < mm:
        if n in a:
            day_mm = day_mm + 31
        elif n in b:
            day_mm = day_mm + 30
        else:
            day_mm = day_mm + 28
        n = n+1
    else:
        num = day_mm + dd
    return num

if y % 4 == 0:
    day = f_r(m, d)
else:
    day = f_n(m, d)
print(day)
