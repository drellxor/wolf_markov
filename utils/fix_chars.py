if __name__ == '__main__':
    with open('../quotes/paccanskie_ponyatiya.txt', 'r') as in_f, open('../dataset/paccanskie_ponyatiya_fixed.txt', 'w') as out_f:
        text = in_f.read()
        text = text.replace('[club60008578|@needy_wolf]\n', '')
        d = {'W': 'Ш',
             'w': 'ш',
             'E': 'Е',
             'e': 'е',
             'T': 'Т',
             'Y': 'У',
             'y': 'у',
             'U': 'И',
             'u': 'и',
             'O': 'О',
             'o': 'о',
             'P': 'Р',
             'p': 'р',
             'A': 'А',
             'a': 'а',
             'H': 'Н',
             'K': 'К',
             'k': 'к',
             'X': 'Х',
             'x': 'х',
             'C': 'С',
             'c': 'с',
             'B': 'В',
             'n': 'п',
             'M': 'М',
             'm': 'т'
             }
        d_ord = {ord(key): ord(value) for key, value in d.items()}
        text = text.translate(d_ord)
        out_f.write(text)
