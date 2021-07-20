list_of_data=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# привожу список к виду
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
position=list_of_data.index('5')
list_of_data[position]='05'
list_of_data.insert(position+1, '"')
list_of_data.insert(position, '"')

position=list_of_data.index('17')
list_of_data.insert(position+1, '"')
list_of_data.insert(position, '"')

position=list_of_data.index('+5')
list_of_data[position]='+05'
list_of_data.insert(position+1, '"')
list_of_data.insert(position, '"')
# меняю строку вида " 05 " на "05"
string=" ".join(list_of_data)
string=string.replace(' " 05 " ',' "05" ')
string=string.replace(' " 17 " ',' "17" ')
string=string.replace(' " +05 " ',' "+05" ')
print(string)