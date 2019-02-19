import locale

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
print(sorted(fruits, key = locale.strxfrm))


import unicodedata
import re
re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
for char in sample: 
	print('U+%04x' % ord(char), char.center(6),
		're_dig' if re_digit.match(char) else '-', 
		'isdig' if char.isdigit() else '-', 
		'isnum' if char.isnumeric() else '-', 
		format(unicodedata.numeric(char), '5.2f'), 
		unicodedata.name(char), sep='\t')