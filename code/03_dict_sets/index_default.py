import sys
import re
import collections

# Mappings with Flexible Key Lookup
## defaultdict: Another Take on Missing Keys

"""Build an index mapping word -> list of occurences"""

WORD_RE = re.compile('\w+')

index = collections.defaultdict(list) # Create a defaultdict with the list constructor as default_factory
with open(sys.argv[1], encoding = 'utf-8') as fp:
	for line_no, line in enumerate(fp, 1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start()+1
			location = (line_no, column_no)
			index[word].append(location) # If word is not initially in the index, the default_factory is called to produce the missing value, which in this case is an empty list that is then assigned to index[word] and returned, so the .append(location) operation always succeeds.

for word in sorted(index, key = str.upper):
	print(word, index[word])





