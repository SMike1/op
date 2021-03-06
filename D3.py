import re

r = re.findall(r'(?:[А-Я]{2,}\s*)+', 'Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН')
for i in range(0, len(r)):
    r[i] = re.sub(r'^\s+|\s+$', '', r[i])

assert r == ['ФГОС', 'ПООП' , 'ФГУ ФНЦ НИИСИ РАН']

'''
for i in range(0, len(r)):
    r[i] = r[i].strip()
assert r == ['ФГОС', 'ПООП' , 'ФГУ ФНЦ НИИСИ РАН']
'''
