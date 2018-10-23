lst = eval(input("Geef lijst met minimaal 10 strings: "))
for word in lst:
    if len(word) > 4:
        lst.remove(word)
if len(lst[-1]) > 4:
    lst.remove(lst[-1])
print(lst)