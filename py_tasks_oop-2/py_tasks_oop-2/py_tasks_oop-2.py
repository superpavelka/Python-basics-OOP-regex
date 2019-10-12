import re
from bs4 import BeautifulSoup as BS

with open('1.txt') as f:
    s = f.read()
# делаем шаблон
pattern = re.compile('Нас уже ([0-9\s]+) человек')
# задание а через регулярные выражания
pers_num_re = re.findall(pattern, s)
print('Количество студентов:', pers_num_re)
# задание б через BS
soup = BS(s, 'html.parser')
# можно через findAll и так более правильно потому что указываем тег атрибут и значение атрибута
pers_num_soup = soup.findAll("span", {"class": "total-users"})
print('Количество студентов:', re.findall(pattern, str(pers_num_soup)))
# можно через стрингу и тег т.к. интересующий нас тег первый
print('Количество студентов:', re.findall(pattern, soup.span.string))
