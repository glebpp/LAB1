units = input("Выберите единицы измерения:\n \
\t1 - граммы,\n \
\t2 - килограммы,\n \
\t3 - тонны,\n \
\t4 - стоп.\n№: ")

while units!='s':
    qty = float(input("Введите значение: "))

    if units == '1':
        print("килограммы: %10.3f" % (qty / 10**3 ))
        print("тонны: %10.3f" % (qty / 10**6 ))
    elif units == '2':
        print("граммы: %10.3f" % (qty * 10**3 ))
        print("тонны: %10.3f" % (qty / 10**3))
    elif units == '3':
        print("граммы: %10.3f" % (qty * 10**6))
        print("килограммы: %10.3f" % (qty * 10 ** 3))

    units=input("Выберите значение: ",end='\r')


