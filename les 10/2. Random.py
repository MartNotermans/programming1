import random
def monopolyworp():
    dobbelsteen_1=random.randrange(1,7)
    dobbelsteen_2=random.randrange(1,7)
    print(dobbelsteen_1,'+',dobbelsteen_2,'=',dobbelsteen_1 + dobbelsteen_2, end="")
    if dobbelsteen_1 == dobbelsteen_2:
        print(' (dubbel)')
        dobbelsteen_1 = random.randrange(1, 7)
        dobbelsteen_2 = random.randrange(1, 7)
        print(dobbelsteen_1, '+', dobbelsteen_2, '=', dobbelsteen_1 + dobbelsteen_2, end="")
    if dobbelsteen_1 == dobbelsteen_2:
        print(' (dubbel)')
        dobbelsteen_1 = random.randrange(1, 7)
        dobbelsteen_2 = random.randrange(1, 7)
        print(dobbelsteen_1, '+', dobbelsteen_2, end="")
    if dobbelsteen_1 == dobbelsteen_2:
        print('= direct naar de gevangenis')
monopolyworp()