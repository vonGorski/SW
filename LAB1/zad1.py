print("Zadanie 1 - Krzysztof Górski")

while True:

    word = input('Write a word or phrase:  ')
    dictionary = {}

    for i in word:
        i = i.lower()
        
        if i in dictionary: 
            dictionary[i] += 1
        else: 
            dictionary[i] = 1

    print("occurency of signs: ", dictionary)

    t = input('end program? (T/F)')
    if t == 'T':
        break

print('End')