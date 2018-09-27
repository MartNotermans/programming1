def standaardprijs(afstandKM):
    if 50 > afstandKM > 0:
        prijs = afstandKM*0.80
    elif afstandKM > 50:
        prijs = 15+afstandKM*0.60
    elif afstandKM < 0:
        prijs = 0
    return prijs
def bepaal_weekend(dag):
    return len(dag) > 0 and dag.lower()[0] == 'z'


afstandKM = eval(input('hoeveel KM ga je reizen? '))
dag = input('welke dag ga je reizen? ')
leeftijd = int(input('wat is uw leeftijd? '))

weekendrit = bepaal_weekend(dag)
prijs = standaardprijs(afstandKM)

def ritprijs (leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            prijs2 = prijs * 0.70
        else:
            prijs2 = prijs * 0.65
    else:
        if weekendrit:
            prijs2 = prijs * 0.60
        else:
            prijs2 = prijs
    return prijs2
prijs2 = ritprijs(leeftijd,weekendrit,afstandKM)
print('u moet €'+str(round(prijs2, 2)),'betalen')