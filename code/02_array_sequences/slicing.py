# Why Slices and Range Exclude the Last Item
l = list(range(10, 70, 10))
print (l[:2])
print(l[2:])

# Slice objects
# s[start:stop:step]
#  If there is no value before the first colon, it means to start at the beginning index of the list
# If there isn't a value after the second colon, it means to go all the way to the end of the list (it saves time as it's not necessary to specify len(s))
s = 'bicycle'
print(s[::3]) # increment the index by 3
print(s[::-1])
print(s[::-2])

invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                 $17.50    3    $52.50
1489  6mm Tactile Switch x20            $4.95     2    $9.90
1510  Panavise Jr. - PV-201             $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240            $34.95    1    $34.95"""

SKU = slice(0,6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]# from the second (not including it) line onwards. note that the 1st line(at position 0 is a blank line)

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# https://www.reddit.com/r/learnpython/comments/acan5b/til_about_slice_objects/
items = []
for item in line_items:
    cleaned_item = {}
    item = item.split()
    cleaned_item["sku"] = int(item[0])
    cleaned_item["description"] = " ".join(item[1:-3])
    cleaned_item["unit_price"] = float(item[-3][1:])
    cleaned_item["quantity"] = int(item[-2])
    cleaned_item["item_total"] = float(item[-1][1:])
    items.append(cleaned_item)
total_cost = sum(item["item_total"] for item in items)
print(total_cost)

# Assigning to Slices
l = list(range(10))
print('list is:')
print(l)
l[2:5] = [20, 30]
print('Now list is:')
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 12]
print(l)
# l[2:5] = 100 # will raise an error. When the target of the assignment is a slice, the right side must be an iterable object, even if it has just one item.
l[2:5] = [100]
print(l)












