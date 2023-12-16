import re


def calculate_index():
    found = {}
    regexp = re.compile("^[а-яё]$")
    for i in range(1, 5):
        with open(f'input/voyna-i-mir-tom-{i}.txt') as tom_file:
            tom = ''.join(tom_file.readlines()).lower()
        for char in tom:
            if not regexp.match(char):
                continue
            found[char] = 1 if char not in found else found[char] + 1
    total_symbols = sum(found.values())
    freq = {char: found[char] / total_symbols for char in found}
    print(f'Частоты: {sorted(freq.items(), key=lambda x: x[1], reverse=True)}')
    print(f'Индекс совпадения: {sum([frequency ** 2 for frequency in freq.values()])}')
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # напишем алфавит так, иначе будут проблемы с "ё"
    for offset in range(1, 17):  # взаимные ИС для отступов s и 33-s одинаковые
        print(f'Индекс взаимного совпадения при отступе {offset}: '
              f'{sum(freq[sym] * freq[alphabet[(alphabet.find(sym) + offset) % 33]] for sym in alphabet)}')


if __name__ == '__main__':
    calculate_index()
