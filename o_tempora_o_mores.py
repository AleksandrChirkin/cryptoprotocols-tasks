import re


def count_statistic():
    found = {}
    regexp = re.compile("^[а-яёa-z]$")
    with open('input/latin_text.txt', encoding='utf-8') as latin_and_russian_text:
        content = ''.join(latin_and_russian_text.readlines()).lower()
    for char in content:
        if not regexp.match(char):
            continue
        found[char] = 1 if char not in found else found[char] + 1
    total_symbols = sum(found.values())
    freq = {char: found[char] / total_symbols for char in found}
    print(f'Частоты: {sorted(freq.items(), key=lambda x: x[1], reverse=True)}')
    print(f'Индекс совпадения: {sum([frequency ** 2 for frequency in freq.values()])}')
    new_found = found.copy()
    for sym in new_found.keys():
        if freq[sym] > 0.027:
            new_found[sym] *= 5
    new_total_symbols = sum(new_found.values())
    new_freq = {char: new_found[char] / new_total_symbols for char in new_found}
    print(f'Частоты: {sorted(new_freq.items(), key=lambda x: x[1], reverse=True)}')
    print(f'Индекс совпадения: {sum([frequency ** 2 for frequency in new_freq.values()])}')


if __name__ == '__main__':
    count_statistic()
