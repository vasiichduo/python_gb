import os

print('\n|--<название проекта>\n\t|--settings\n\t|--mainapp\n\t|--adminapp\n\t|--authapp\n' + '-' * 66)
gen_dir = input('Введите название проекта: ')
if not os.path.isdir(gen_dir):
    os.mkdir(gen_dir)
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in dir_list:
    if not os.path.isdir(os.path.join(gen_dir, i)):
        os.mkdir(os.path.join(gen_dir, i))
    else:
        print(f'Папка {i} уже существует!')
print('\nСтартер успешно создан!')