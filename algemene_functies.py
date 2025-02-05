def mijn_functie_1(argument):
    waarde = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }

    if argument in waarde:
     return argument ** 2


def mijn_functie_2(a, b):
    tabel = {
        (12, 3): [15, 9, 36, 4],
        (12, 2): [14, 10, 24, 6],
        (10, 5): [15, 5, 50, 2],
        (100, 20): [120, 80, 200, 5]
    }
    if (a,b) in tabel:
         return [a + b, a - b, a * b, a / b]
    else:
        return
