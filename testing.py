import re


def normalize(s):
    text = []
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a.upper(), b.upper())
        print(f'''a: {a}, b: {b}, str: {s}''')
    return s


print(normalize("¡HÓLÁ, MÚNDÓ!"))


def join():
    word_li = ['E', 'X', 'P', 'L', 'O', 'S', 'I', 'O', 'N']
    return ''.join(word_li)


print(join())


def dictionary():
    word = "andres"
    index_letter = {i[0]: i[1] for i in enumerate(word)}
    return index_letter


def search_dates_of_birth(cadena):
    patron = r'(\d{2})-(\d{2})-(\d{4})'
    res = re.findall(patron, cadena)
    fechas = []
    i = 0
    for el in res:
        text = '-'.join(res[i])
        fechas.append(text)
        i = i + 1
    return fechas

print(search_dates_of_birth("as-as-asdf 1s-s2-2345 04-24-1946 abc-defg-hijk ABC-DEFG-HIJK 03-23-1996 f3g5, 03-23-1936 asdcadca 03-23-1996 345435"))