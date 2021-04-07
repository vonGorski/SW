file = open('tekst.txt', "r")
line = file.read() 
lines = line.splitlines()
dictionary={}
key = ""
for i in range(len(lines)):   
    lines[i].rstrip()
    r=''.join(reversed(lines[i])) 
    if lines[i]==r:   
           dictionary.setdefault('full phrase palindromes: ',[]).append(lines[i])

    lin=lines[i].split()
    for j in range(len(lin)):
        r=''.join(reversed(lin[j]))
        if lin[j]==r:   
           dictionary.setdefault('single palindromes: ',[]).append(lin[j])

for keys,values in dictionary.items():
    print(keys)
    print(values)

