def fix_text(text: str):
    if text.startswith('-') or text.startswith('—'):
        return ''

    text = text.replace('[club60008578|@needy_wolf]', '').replace('\n', ' ')
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

    if not text.endswith('.') or text.endswith('!') or text.endswith('?'):
        text += '.'

    return text
