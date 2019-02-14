import os

# Handling Text Files
open('cafe.txt', 'w', encoding='utf_8').write('café')
print(open('cafe.txt').read())

######
fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
fp.close()

os.stat('cafe.txt').st_size
fp2 = open('cafe.txt')
print(fp2)
print(fp2.read())
fp3 = open('cafe.txt', encoding='utf_8')
print(fp3)
print(fp3.read())
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())