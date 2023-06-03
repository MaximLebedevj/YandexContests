#!/usr/bin/env python3

d = {'А': 'A',
     'Б': 'B',
     'В': 'V',
     'Г': 'G',
     'Д': 'D',
     'Е': 'E',
     'Ё': 'E',
     'Ж': 'Zh',
     'З': 'Z',
     'И': 'I',
     'Й': 'I',
     'К': 'K',
     'Л': 'L',
     'М': 'M',
     'Н': 'N',
     'О': 'O',
     'П': 'P',
     'Р': 'R',
     'С': 'S',
     'Т': 'T',
     'У': 'U',
     'Ф': 'F',
     'Х': 'Kh',
     'Ц': 'Tc',
     'Ч': 'Ch',
     'Ш': 'Sh',
     'Щ': 'Shch',
     'Ы': 'Y',
     'Э': 'E',
     'Ю': 'Iu',
     'Я': 'Ia', 
     'Ь': '',
     'Ъ': ''}

s = input()
for symbol in s:
    if symbol.upper() in d.keys():
        if symbol.isupper():
            print(d[symbol], end='')
        else:
            print(d[symbol.upper()].lower(), end='')
    else:
        print(symbol, end='')

