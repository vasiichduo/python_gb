list_of_data_result = []
list_of_data = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for element in list_of_data:
    list_of_data_result.append(element)

i = 0
while i < len(list_of_data_result):
    print(list_of_data_result[i], 'это', type(list_of_data_result[i]))
    i+=1
