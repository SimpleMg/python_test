def tri_insertion(liste):
    for i in range(1,len(liste)):
        cle = liste[i]
        j = i - 1
        while cle < liste[j] and j >= 0:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = cle
    return liste

liste_a_trier = [5,10,4,6,1,3]
print(tri_insertion(liste_a_trier))
