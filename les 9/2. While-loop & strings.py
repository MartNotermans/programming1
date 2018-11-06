while True:
    string=input('Geef een string van 4 letters:')
    if len(string) is not 4:
        print(string,'heeft',len(string),'letters')
    else:
        print('Inlezen van correcte string:',string,'is geslaagd')
        break
