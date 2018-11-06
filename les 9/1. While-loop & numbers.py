lst = []
while True:
    if 0 not in lst:
        userinput = eval(input('geef een getal:'))
        lst.append(userinput)
    else:
        print('er zijn', len(lst), 'getallen ingevoerd, de som is:', sum(lst))
        break