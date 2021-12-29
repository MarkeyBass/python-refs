# https://docs.python.org/3/library/struct.html

from struct import pack, unpack

x = 2.51

# d - double
# < - little endian
data = pack('<d', x)

print(data)
print(tuple(data))

print(unpack('<d', data))


# f - floating point
data = pack('<f', x)

print(data)
print(tuple(data))


print(unpack('<f', data))


y = "Hello"
data = pack('10s', y.encode('ascii'))
print(data)
print(tuple(data))

print(unpack('10s', data))

