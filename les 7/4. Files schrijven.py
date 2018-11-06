while True:
    import datetime
    vandaag = datetime.datetime.today()
    naam = input('welke hardloper kwam er voorbij? ')
    outfile = open("hardlopers.txt", "a")
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, "+naam +"\n")

    outfile.write(s)
    outfile.close()