# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
class Word:
    def __init__(self, text):
        self.text = text


class Sentence:
    def __init__(self, content):
        self.content = content

    def show(self, words):
        sentence = ''
        count = 0
        for word_number in self.content:
            try:
                if (count == 0):
                    sentence += words[word_number].text.capitalize() + ' '
                elif count != len(self.content) - 1:
                    sentence += words[word_number].text + ' '
                else:
                    sentence += words[word_number].text + '.'
                count += 1
            except IndexError:
                print('Некорректное значение переменной content = ', self.content[count], '(метод show)')
                print('В переданном вами списке всего', len(words), 'слов', '- максимальный индекс равен',
                      len(words) - 1)
        print(sentence)

    def show_parts(self, words):
        parts = ''
        count = 0
        for word_number in self.content:
            try:
                parts += words[word_number].part() + ' '
                count += 1
            except IndexError:
                print('Некорректное значение переменной content = ', self.content[count], '(метод show_parts)')
                print('В переданном вами списке всего', len(words), 'слов', '- максимальный индекс равен',
                      len(words) - 1)
        print(list(set(parts.split())))


# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и сделайте свойство grammar защищённым.
class Noun(Word):
    __grammar = 'сущ'

    # 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
    def part(self):
        return 'существительное'


class Verb(Word):
    __grammar = 'гл'

    # 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
    def part(self):
        return 'глагол'


# пример создания экземпляра нового класса
word_example = Noun('компьютер')
# пример доступа к приватной переменной
try:
    print(word_example.__grammar)
except AttributeError:
    print('Попытка доступа к приватной переменной!')

words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))
words.append(Verb("ел"))
words.append(Noun("мясо"))
words.append(Noun("кота"))
print('Примеры предложений:')
sentence = Sentence([0, 1, 2])
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
sentence.show(words)
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
sentence.show_parts(words)

sentence = Sentence([3, 4, 5])
sentence.show(words)
sentence.show_parts(words)

sentence = Sentence([0, 1, 6])
sentence.show(words)
sentence.show_parts(words)
