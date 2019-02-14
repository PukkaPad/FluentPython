import array
import struct

# encoding and decoding
s = 'café'
print(len(s))  # will print 4

b = s.encode('utf-8')
print(b)  # will print: b'caf\xc3\xa9'
# bytes literals start with a b prefix.
# bytes b has five bytes (the code point for “é” is encoded as two bytes
# in UTF-8).
print(len(b))
print(b.decode('utf-8'))

# A five-byte sequence as bytes and as bytearray
cafe = bytes('café', encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[1])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# Initializing bytes from the raw data of an array
# Typecode 'h' creates an array of short integers (16 bits).
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)  # These are the 10 bytes that represent the five short integers.

# Using memoryview and struct to inspect a GIF image header
fmt = '<3s3sHH'  # struct format: < little-endian; 3s3s two sequences of 3 bytes; HH two 16-bit integers
with open('python.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(header)
print(bytes(header))
print('type, version, width, and height', struct.unpack(fmt, header))
del header
del img

# Basic Encoders/Decoders
for codec in ['latin_1', 'utf_8', 'utf_16']:
    # note: encode.encode('latin1')  # Throws UnicodeEncodeError, proves that
    # this can't be expressed in ISO-8859-1.
    print(codec, 'El Niñ̃o'.encode(codec, errors='replace'), sep='\t')

# Coping with UnicodeEncodeError
city = 'São Paulo'
print('utf-8: ', city.encode('utf_8'))  # The 'utf_?' encodings handle any str.
print('utf-16: ', city.encode('utf_16'))
print('iso8859_1: ', city.encode('iso8859_1'))
# print('cp434', city.encode('cp434')) # error!
# handler silently skips characters that cannot be encoded; this is
# usually a very bad idea
print('cp437 - ignore erros: ', city.encode('cp437', errors='ignore'))
# ubstitutes unencodable characters with '?'; data is lost, but users will
# know something is amiss.
print('cp437 - replace  errors: ', city.encode('cp437', errors='replace'))
print('cp437 - replace unencodable char with XML entity: ',
      city.encode('cp437', errors='xmlcharrefreplace'))

# Decoding from str to bytes: success and error handling
octets = b'Montr\xe9al'
print(octets)
print(octets.decode('cp1252'))  # Montréal
print(octets.decode('iso8859_7'))  # Montrιal
print(octets.decode('koi8_r'))  # MontrИal
# print(octets.decode('utf_8')) # UnicodeDecodeError: 'utf-8' codec can't
# decode byte 0xe9 in position 5: invalid continuation byte
print(octets.decode('utf_8', errors='replace'))  # Montr�al


