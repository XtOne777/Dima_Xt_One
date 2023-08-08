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
for i in a:
    if len(list(filter(lambda x: x.isdigit(), list(i)))) == len(i):
        print(i + " - число")
        continue
    print(i + " - не число")
