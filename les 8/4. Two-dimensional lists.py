studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    student1 = sum(studentencijfers[0]) / len(studentencijfers[0])
    student2 = sum(studentencijfers[1]) / len(studentencijfers[1])
    student3 = sum(studentencijfers[2]) / len(studentencijfers[2])
    student4 = sum(studentencijfers[3]) / len(studentencijfers[3])
    return student1, student2, student3, student4

def gemiddelde_van_alle_studenten(studentencijfers):
    student1 = sum(studentencijfers[0]) / len(studentencijfers[0])
    student2 = sum(studentencijfers[1]) / len(studentencijfers[1])
    student3 = sum(studentencijfers[2]) / len(studentencijfers[2])
    student4 = sum(studentencijfers[3]) / len(studentencijfers[3])
    gemmiddelde = (student1+student2+student3+student4) / 4
    return gemmiddelde

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))