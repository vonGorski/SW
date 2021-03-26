import re
file = open('Mails.txt', "r")
lines = file.readlines() 
dictionary={}
for i in range(len(lines)):       
    if re.search(r'(From|from|od|nadawca|autor)',lines[i]):
         dictionary['FROM']=re.search(r'[\w\.−]+@[\w\.−]+',lines[i]).group()
    elif re.search(r'(To|to|do|odbiorca)',lines[i]):
         dictionary['TO']=re.search(r'[\w\.−]+@[\w\.−]+',lines[i]).group()
    elif re.search(r'(subject|temat)',lines[i]):
         lin=lines[i].split(':')
         dictionary['SUBJECT']=lin[1]
    elif re.search(r'(date|data)',lines[i]):
         lin=lines[i].split(':')
         dictionary['DATE']=lin[1]
print(dictionary)

