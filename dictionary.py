#import json

filepath = "email.txt"
f = open(filepath, "r", encoding="utf-8")
s = (str(f.read()))
table={}
table2={}
head={}
k=int(0)

# dividing lines
for line in s: 
    table=s.split('\n')

for i in range(len(table)):
    if not(table[i].startswith(" ") or table[i].startswith("-")):  #if it starts with this chars, skip
        table2[k]=table[i].split(': ',1) # dividing by 2 strings
        k=k+1

print("Dictionary:")
for i in range(0, k-1):
    if (len(table2[i]) == 2): #if there's 2 elements in one line
        head[table2[i][0]] = table2[i][1]

for left, right in head.items():
    print(left,":",right)
#print(json.dumps(head, indent=4))
