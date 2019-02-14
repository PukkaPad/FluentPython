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