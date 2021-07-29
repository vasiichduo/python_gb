def thesaurus(*value):
    result = {}
    for full_name in value:
        '''
        Нахожу первую букву фамилии,
        где в первой итерации 'Виталий Абрамов' full_name[8] = [А]
        '''
        x = full_name.rindex(' ')+1 # работает только с заглавными буквами фамилии
        if full_name[x] in result:
            '''
            Добавляю в словарь фамилий словарь с именем и полную фамилию и имя
            '''
            result[full_name[x]].setdefault(full_name[0], [full_name])
        else:
            result.setdefault(full_name[x], {})
            result[full_name[x]].setdefault(full_name[0], [full_name])
    return result
print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
