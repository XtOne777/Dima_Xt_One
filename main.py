# Одиночные Типы
integer = int(6)
float_example = float()
string = str()
boolean = bool()

# Списки, сборки
lol = int()
asdas = int()

tuple_example = (1, 2, 3, "21asd")
dictionary = {1, 2, 3, 4, "asdasd"}

a = input().split(";")
b = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
for i in a:
    flag = True
    for k in i:
        if k not in b:
            flag = False
    if flag:
        print(i + " - число")
        continue
    print(i + " - не число")
