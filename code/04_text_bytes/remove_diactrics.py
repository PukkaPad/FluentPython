#  Function to remove all combining marks
import unicodedata
import string

def shave_marks(txt):
	"""Remove all diacritic marks"""
	norm_txt = unicodedata.normalize('NFD', txt)
	shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
	return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • 1⁄2 cup of ŒtkerTM caffè latte • bowl of açaí.”'
print(shave_marks(order))
Greek = 'Ζέφυρος, Zéfiro'
print(shave_marks(Greek))

def shave_marks_latin(txt):
	"""Remove all diacritic marks from Latin base characters""" 
	norm_txt = unicodedata.normalize('NFD', txt)
	latin_base = False
	keepers = []
	for c in norm_txt:
		if unicodedata.combining(c) and latin_base: 
			continue # ignore diacritic on Latin base char
		keepers.append(c)
			# if it isn't combining char, it's a new base char 
		if not unicodedata.combining(c):
			latin_base = c in string.ascii_letters 
	shaved = ''.join(keepers)
	return unicodedata.normalize('NFC', shaved)

order = '“Herr Voß: • 1⁄2 cup of ŒtkerTM caffè latte • bowl of açaí.”'
print(shave_marks_latin(order))
print(shave_marks_latin(Greek))
