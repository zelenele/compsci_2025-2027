Lista_sigiemek = [9,5,4,3,2,1,6]
Lista_sigiemek2 = [65,3,2,1]
Lista_sigiemek23 = [2,55,31,2]
Lista_biggest = [Lista_sigiemek2,Lista_sigiemek,Lista_sigiemek23]

def bialas(Lista_biggest):
    for Lista in Lista_biggest:
        print(Lista)
        for x in Lista:
            the_biggest = Lista(0)
            if x > the_biggest:
                the_biggest = x
    print(the_biggest)
bialas(Lista_biggest)
