rate = int(input('Введите процент: '))
for rate in range(rate):
    if rate % 10 == 1 and rate % 100 != 11:
        print(rate, 'процент')
    elif 1 < rate %  10 < 5 and not 11 < rate % 100 < 15:
        print(rate, 'процента')
    else:
        print(rate, 'процентов')