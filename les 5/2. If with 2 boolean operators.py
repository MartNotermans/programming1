leeftijd = input('hoe oud bent u? ')
paspoort = input('bent u in het bezit van een nederlands paspoort? ja of nee ')
if leeftijd > '17' and paspoort == 'ja':
    print ('u mag stemmen')
else:
    print ('u mag niet stemmen')
