# 1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
# 2. Добавьте свойства text (класс будет хранить слово) и part (часть речи, которой является слово.
# Например, существительное, прилагательное и т.п.). Для добавления свойств воспользуйтесь методом __init__.
class Word:
    def __init__(self, text, part):
        self.text = text
        self.part = part


# 4. Создайте класс Sentence. (по аналогии с п. 1).
# 5. Добавьте свойство content. (по аналогии с п. 2).
class Sentence:
    def __init__(self, content):
        self.content = content

    # 7. Добавьте в класс Sentence метод show, составляющий предложение.
    # Метод должен перебирать числа из свойства content и подставлять соответствующие слова, которые
    # хранятся в свойстве text экземпляров класса Word. Данные извлекаем из списка words, который получили на
    # прошлом шаге. При соединении слов в предложение не забудьте добавить пробел между словами.
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

    # 8. Добавьте в класс Sentence метод show_parts, отображающий, какие части речи входят в предложение.
    # По аналогии с п. 7 перебирайте в цикле числа из свойства content и сохраняйте результат в отдельный список.
    # Учтите, что части речи могут повторяться, но список не должен содержать дубликаты.
    def show_parts(self, words):
        parts = ''
        count = 0
        for word_number in self.content:
            try:
                parts += words[word_number].part + ' '
                count += 1
            except IndexError:
                print('Некорректное значение переменной content = ', self.content[count], '(метод show_parts)')
                print('В переданном вами списке всего', len(words), 'слов', '- максимальный индекс равен',
                      len(words) - 1)
        print(list(set(parts.split())))


words_example = [["собака", "сущ"],
                 ["ела", "глагол"],
                 ["колбасу", "сущ"],
                 ["вечером", "наречие"],
                 ["большая", "прилагательное"]]

# 3. Создайте экземпляр класса Word, передав в качестве параметров любое слово и указав его часть речи.
word_example = Word('компьютер', 'сущ')
print('Пример экземпляра класса:', word_example.text, word_example.part)
# 6. Создайте из массива (можете взять приведённый выше или придумать свой) список,
# каждый элемент которого является экземпляром класса Word.
# Примечание: список list (назовём его words) — отдельная переменная, не относящаяся к классам Word и Sentence.
words = [Word(word[0], word[1]) for word in words_example]
print('\nИсходный массив слов:')
for word in words:
    print(word.text, word.part)
# Вывод примеров предложений
print('\nПостроение предложения 1:')
sentence = Sentence([0, 1, 2])
sentence.show(words)
sentence.show_parts(words)
print('\nПостроение предложения 2:')
sentence = Sentence([3, 0, 1, 2])
sentence.show(words)
sentence.show_parts(words)
print('\nПостроение предложения 3:')
sentence = Sentence([3, 4, 0, 1, 2])
sentence.show(words)
sentence.show_parts(words)
print('\nПостроение предложения c некорректной инициализацией параметров:')
sentence = Sentence([3, 4, 0, 1, 5])
sentence.show(words)
sentence.show_parts(words)
