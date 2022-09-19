try:
    A = float(input('Введите A: '))
    B = float(input('Введите B: '))
    X = float(input('Введите X: '))
    try:
        if (X > 4):
            y = (4 * pow(A, 2) + B*X) / (B+X)
        else:
            y = 3 * pow((A+B+X), 2)
        print('y=', format(y,'.2f'))
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные")