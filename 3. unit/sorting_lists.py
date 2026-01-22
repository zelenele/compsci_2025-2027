lista_sortowana = [4,2,13,8,10,5,6,27]

for numbers in lista_sortowana:
    n = 0
    if lista_sortowana[n] <= lista_sortowana[ n + 1]:
        n += 1
    else: 
        popnik = lista_sortowana.pop(n +1)
        lista_sortowana.insert(0, popnik)
        n += 1