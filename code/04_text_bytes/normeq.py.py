from unicodedata import normalize, name


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())

# Normalizing Unicode for Saner Comparisons
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)

print(nfc_equal(s1, s2))


print(nfc_equal('A', 'a'))

print(f'Length of normalized s1 is {len(s1)} and length of normalized s2 is {len(s2)}')

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))

print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

### 
ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

## 
half = '1⁄2'
print(normalize('NFKC', half))
four_squared = '42'
print(normalize('NFKC', four_squared))
micro = 'μ'
micro_kc = normalize('NFKC', micro) 
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))

# Case Folding
micro = 'μ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_kc)
eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)




