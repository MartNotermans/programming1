def studentencijfers(cijfers):
    for i in cijfers:
        if cijfers[i]>9:
            print(i, cijfers[i])

cijfers={'jessie': 9.4, 'piet': 6.7,'sophie': 4.3,'stijn': 4.2,'jordi': 9.6,'eric': 9.4,'joost': 8.9,'wiebe': 5.7}

studentencijfers(cijfers)