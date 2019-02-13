import array

# encoding and decoding
s = 'café'
print(len(s)) # will print 4

b = s.encode('utf-8')
print(b) # will print: b'caf\xc3\xa9'
#bytes literals start with a b prefix.
print(len(b)) # bytes b has five bytes (the code point for “é” is encoded as two bytes in UTF-8).
print(b.decode('utf-8'))

# A five-byte sequence as bytes and as bytearray
cafe = bytes('café', encoding = 'utf-8')
print(cafe)
print(cafe[0])
print(cafe[1])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# Initializing bytes from the raw data of an array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # Typecode 'h' creates an array of short integers (16 bits).
octets = bytes(numbers)
print(octets) # These are the 10 bytes that represent the five short integers.

# Using memoryview and struct to inspect a GIF image header