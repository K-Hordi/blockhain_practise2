import binascii
import sys


def pad(mystr, size, mode):
  padding_size=2*size
  if mode=='l':
    mystr = mystr + "0"*(padding_size - len(mystr))
  else:
    mystr = "0"*(padding_size - len(mystr)) + mystr 
  return mystr


def hexToLittle(value):
    a=pad(value[:2*size], size,'l')
    return int.from_bytes(binascii.unhexlify(a),byteorder='little')

def hexToBig(value):
    a=pad(value[:2*size], size,'l')
    return int.from_bytes(binascii.unhexlify(value),byteorder='big')

def littleToHex(value):
    return hex(value)
def bigToHex(value):
    return hex(value)

print("Print hex value (short)")
a=input()

print("Print number of bytes:")
size = int(input())



print(f"Value: {a}\nNumber of bytes: {size}\nLittle-endian: {hexToLittle(a)}\nBig-endian: {hexToBig(a)}\nLitte to Hex:  {littleToHex(hexToLittle(a))}\nBig to Hex:  {bigToHex(hexToBig(a))}")

