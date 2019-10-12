import re


# функция создания ТОП списка
# word_value - словарь слово : количество повторов
# num - количество мест в топе
def sort_top(word_value, num):
    register = list()
    l_dict = str(len(word_value))
    for i in word_value.items():
        l_word = str(i[1])
        register.append((len(l_dict) - len(l_word)) * '0' + str(i[1]) + ' ' + i[
            0])  # разворачиваем и добавляем нули перед количеством для сортировки, делаем слияние элементов = '00012 слово'
    register.sort(reverse=True)
    top_list = list()
    top = {}
    count = 1
    for j in register:
        top[count] = j.split(' ')  # получаем словарь типа {1: (количество, слово)}
        top[count][0] = int(top[count][0])
        if count == num:
            break
        count += 1
    return top


# Задание 1 получаем текст из файла
text = ''
with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text += line
print('Текст из файла:')
print(text)
# Задание 2 разбиваем текст на предложения
# делаем список всех предложений
sentence_pattern = re.compile('\. |\! |\? |\.\n|\!\n|\?\n')
sentence_lst = re.split(sentence_pattern, text)
print('Список всех предложений:')
print(sentence_lst)
# Задание 3
# делаем список всех слов
words_pattern = re.compile('[a-zA-Zа-яА-ЯёЁ]{4,}')
words_lst = words_pattern.findall(text)
# делаем список всех слов в одном регистре, чтобы при подсчете слов учитывать слова с большой и маленькой буквы
words_lst_lower = []
for word in words_lst:
    words_lst_lower.append(word.lower())
print('Список всех слов:')
print(words_lst)
print('Список всех слов(все буквы в нижнем регистре):')
print(words_lst_lower)
# делаем словарь всех слов, чтобы исключить повторы
words_set = set(words_lst_lower)
print('Словарь всех слов, соответственно без повторов(все буквы в нижнем регистре):')
print(words_set)
# делаем словарь содерджащий key - слово , value - количество повторов
word_value = {}
for word_in_set in words_set:
    count = 0
    for word_in_lst in words_lst_lower:
        if word_in_set == word_in_lst:
            count += 1
    word_value[word_in_set] = count
print('Словарь всех слов,key - слово, value - количество повторов(все буквы в нижнем регистре):')
print(word_value)
# создаем словарь топ-10 слов
top_10 = sort_top(word_value, 10)
print('Топ-10 слов:')
print(top_10)
# Задание 4
urls_pattern = re.compile('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%]+')
print('Список всех url:')
print(urls_pattern.findall(text))
# Задание 5
domen_pattern = re.compile('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w\-?=%]+')
print('Список всех доменов:')
d_lst = domen_pattern.findall(text)
print(d_lst)
# делаем список всех слов в одном регистре, чтобы при подсчете слов учитывать слова с большой и маленькой буквы
d_lst_lower = []
for word in d_lst:
    d_lst_lower.append(word.lower())
print('Список всех доменов(нижний регистр):')
print(d_lst_lower)
# делаем словарь всех слов, чтобы исключить повторы
d_set = set(d_lst_lower)
print('Словарь всех доменов(нижний регистр):')
print(d_set)
# делаем словарь содерджащий key - слово , value - количество повторов
d_value = {}
for word_in_set in d_set:
    count = 0
    for word_in_lst in d_lst_lower:
        if word_in_set == word_in_lst:
            count += 1
    d_value[word_in_set] = count
print('Словарь всех доменов, key - домен, value - количество повторов(нижний регистр):')
print(d_value)
# создаем словарь топ-1 слов
print('Топ-1 домен:')
top_1 = sort_top(d_value, 1)
print(top_1)
# Задание 6
new_text = re.sub(urls_pattern, 'Ссылка отобразится после регистрации', text)
print('Текст из файла с замененными url:')
print(new_text)
