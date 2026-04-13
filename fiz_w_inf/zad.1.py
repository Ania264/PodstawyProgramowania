chwila = 1
t = 0
while t <= 10:
    x = 2 * t - 6
    y = 4 * t - 5 * t ** 2
    '''if (chwila - 1) % 200 == 0:
        print(x, y)'''
    if chwila % 200 == 1:
        print(x,y)
    t += 0.01
    chwila += 1
    