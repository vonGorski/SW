d = {}

with open('tekst.txt') as f:
    for l in f:
        print(l[:-1])
        for x in l:
            x = x.lower()
            if x != ' ' and x != '\n': #Ni e z l i c z a s p a c j i i
                                        #z n a k o w n o w e j l i n i
                if x in d: #Gdy z n a k s i e p o w t a r z a
                    d[x] += 1
                else: #Gdy z n a k j e s z c z e n i e w y s t a p i l
                    d[x] = 1

print("Liczba wystapien znakow w calym tekscie:", d)