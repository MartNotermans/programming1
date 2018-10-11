filename = "kaartnummers"
file = open(filename, "r")
for line in file:
     lst = line.split(",")
     kaartnummer = lst[0]
     naam = lst[1]
     print ('{} heeft kaartnummer {}'. format(naam.strip(),kaartnummer))