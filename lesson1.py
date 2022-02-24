name = "ксения"
print(name)
age = "19"
print(age)
print(name+name+name+name+name)

zname = input("Как вас зовут?")
xage = input("Сколько вам лет?")
print("Привет, ", zname)
print("Только возраст никогда не меняется в лучшую сторону)")

cage=int(xage)
if cage>=18:
    print("песок с тебя так и сыпется")
else:
    print("мммм, школьникам тут не рады")
a=(name[-3:])
print(name[1:-1])
print(a[::-1])
print(name[0:5])
print(len(name))

sum=0
pro=1
while cage > 0:
    b = cage % 10
    sum = sum + b
    pro = pro * b
    cage = cage // 10
print(sum)
print(pro)

lowerzname = zname.lower()
upperzname = zname.upper()
print(lowerzname)
print(upperzname)
capitalizezname = name.capitalize()
swapcasezname = capitalizezname.swapcase()
print(capitalizezname)
print(swapcasezname)

proverkaname = zname.isalpha()
if proverkaname != True:
    print("имя не корректно")
v=0
vage=int(xage)
if vage > 150:
    v=v+1
if vage < 0:
    v=v+1
if v!=0:
    print("возраст не корректен")

vopros = input("Сколько будет 2*2+2?")
proverka = vopros.isdigit()
if proverka != True:
    print("ответ не корректен")
else:
    vvopros = int(vopros)
    if vvopros == 6:
        print("Верно")
    else:
        print("Ошибка")