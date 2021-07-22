def num_translate(value):
    rus = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}
    eng = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    for eng_key, v in eng.items():
        if v == value:
            return rus.get(eng_key)
num = str(input("Ведите число на английском (one, two, three ... ten):"))
if num.istitle() == True:
    print(num_translate(num.lower()).title())
else:
    print(num_translate(num))