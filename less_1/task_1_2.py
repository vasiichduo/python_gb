list_cubes = []
list_cubes_increase = []
sum_list=0

for i in range(1,1000,2):
    list_cubes.append(i ** 3)

for ind, val in enumerate(list_cubes):
    sum_digits=  0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_list += list_cubes[ind]

print(sum_list)

for m in list_cubes:
    list_cubes_increase.append(m + 17)

sum_list = 0

for ind, val in enumerate(list_cubes_increase):
    sum_digits=  0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_list += list_cubes_increase[ind]

print(sum_list)