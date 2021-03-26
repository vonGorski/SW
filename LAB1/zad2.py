print("zad 2 Krzysztof Górski")
dictionary = {}
with open('tekst.txt') as file:
    print("text from file: ")
    for file_text in file:
        print(file_text[:-1])
        for i in file_text:
            i = i.lower()
            if i != '\n': 
                if i in dictionary: 
                    dictionary[i] += 1
                else:
                    dictionary[i] = 1
print("occurency of signs in file: ", dictionary)