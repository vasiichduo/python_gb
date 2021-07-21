list_of_data=[57.8, 46.51, 97.09, 43.44, 44.76, 88, 12, 66.07, 76, 99]
print(list_of_data)

#исходный список с ценами
print('\n Все цены (Исходный список): ')
i=0
while i < len(list_of_data):
    price=float(list_of_data[i])
    rub=int(price)
    penny=int(100 * (price - rub)+0.1)
    i+=1
    if penny <= 10:
        penny=f'{penny:0{2}}'
    print(rub,'руб',penny,'коп',end = ', ')

#исходный список по возрастанию
id_before_sort_object=id(min(list_of_data))  # id объекта с минимальным значением до сортировки по возрастанию
list_of_data.sort()                          # сортировка по возрастанию
id_after_sort_object=id(min(list_of_data))   # id объекта с минимальным значением после сортировки по возрастанию

print('\n Все цены по возрастанию (Исходный список. Объект из списка не изменялся -',id_before_sort_object==id_after_sort_object,'): ')
i=0
while i < len(list_of_data):
    price=float(list_of_data[i])
    rub=int(price)
    penny=int(100 * (price - rub)+0.1)
    i+=1
    if penny <= 10:
        penny=f'{penny:0{2}}'
    print(rub,'руб',penny,'коп',end = ', ')

#новый список по убыванию
list_of_data_reverse=[]
i=0
for i in range(len(list_of_data)):
    list_of_data_reverse.append(list_of_data[i])
print('\n Все цены по убыванию (новый список): ')
i=0
list_of_data_reverse.sort(reverse = True)
while i < len(list_of_data_reverse):
    price=float(list_of_data_reverse[i])
    rub=int(price)
    penny=int(100 * (price - rub)+0.1)
    i+=1
    if penny <= 10:
        penny=f'{penny:0{2}}'
    print(rub,'руб',penny,'коп',end = ', ')

#Список 5 самых дорогих товаров
print('\n ТОП-5 цен : ')
i=0
while i < len(list_of_data_reverse[0:5]):
    price=float(list_of_data_reverse[i])
    rub=int(price)
    penny=int(100 * (price - rub)+0.1)
    i+=1
    if penny <= 10:
        penny=f'{penny:0{2}}'
    print("ТОП-{0}:".format(i),rub,'руб',penny,'коп')
