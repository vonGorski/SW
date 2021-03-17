print("Zad1")



s = "Jestem bardzo dobrym studentem"
d = {}

for x in s:
    x = x.lower()
    if x != ' ': #Ni e z l i c z a s p a c j i
        if x in d: #Gdy z n a k s i e p o w t a r z a
            d[x] += 1
        else: #Gdy z n a k j e s z c z e n i e w y s t a p i l
            d[x] = 1

print("Liczba wystapien:", d)