print('{0:>3}{1:>9}'.format('F','C'))


def table():
    def convert(tempC):
        tempF = tempC * 1.8 + 32
        print('{0:>5}\t{1:>5}'.format(tempF, x))
    for x in range(-30,50,10):
        convert(x)


table()