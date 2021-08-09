with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = [(i[0:i.find(' ')], i[i.find('G'):i.find('/d')].strip(),
               i[i.find('/d'):i.find('H')].strip()) for i in f]
x = {}
for i in result:
    if i[0] not in x:
        x.setdefault(i[0], 1)
    else:
        x[i[0]] += 1
spam = {k: v for k, v in x.items() if max(x.values()) == v}
print(spam)