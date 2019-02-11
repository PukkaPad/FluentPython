import sys
import re

# Overview of Common Mapping Methods

## Handling Missing Keys with setdefault

"""Build an index mapping word -> list of occurences"""
WORD_RE = re.compile('\w+')
index = {}

# with open(sys.argv[1], encoding='utf-8') as fp:
#     print(fp)
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start()+1
#             location = (line_no, column_no)
#             # this is ugly; coded like this to make a point 
#             occurrences = index.get(word, []) # dict.get(key, default = None)
#             occurrences.append(location)
#             index[word] = occurrences
# # print in alphabetical order
# for word in sorted(index, key = str.upper):
#     print(word, index[word])
# to run: python3 common_mapping_methods.py ./zen-of-python.txt

# improvement:
with open(sys.argv[1], encoding='utf-8') as fp:
  print(fp)
  for line_no, line in enumerate(fp, 1):
      for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location) # dict.setdefault(key, default=None). If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
for word in sorted(index, key = str.upper):
    print(word, index[word])

# Mappings with Flexible Key Lookup



