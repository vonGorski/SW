list=[ 8, 9, 10, 21, 54, 6576, 123, 111]
while True:
    x = int(input("Add your number: "))
    list.append(x)
    for i in enumerate(list):
        print(i)
    print("index: ",list.index(min(list)))
    print("min: ", min(list))
    t = input('end program? (T/F)')
    if t == 'T':
        break
print('End')