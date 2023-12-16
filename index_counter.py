import re


def calculate_index():
    found = {}
    regexp = re.compile("^[а-яёА-ЯЁ]$")
    for i in range(1, 5):
        with open(f'input/voyna-i-mir-tom-{i}.txt') as tom_file:
            tom = ''.join(tom_file.readlines()).replace(' ', '').replace('\n', '').replace('\t', '').lower()
        for char in tom:
            if not regexp.match(char):
                continue
            if char not in found:
                found[char] = 1
            else:
                found[char] += 1
    total_symbols = sum(found.values())
    freq = {char: found[char] / total_symbols for char in found}
    print(f'Индекс совпадения: {str(sum([frequency ** 2 for frequency in freq.values()]))}')


if __name__ == '__main__':
    calculate_index()
