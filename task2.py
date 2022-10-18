
import sys


def pad(mystr, size):
  padding_size=2*size
  mystr = mystr + "0"*(padding_size - len(mystr))
  return mystr



def hexToLittle(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
 
    for i in range(0,length, 1) :
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
 
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
 
    return dec_val
    

def hexToBig(hexval):
    length = len(hexval)
    base = 1
    dec_val = 0
    for i in range(length - 1, -1, -1):
        if hexval[i] >= '0' and hexval[i] <= '9':
            dec_val += (ord(hexval[i]) - 48) * base
            base = base * 16
 
        elif hexval[i] >= 'A' and hexval[i] <= 'F':
            dec_val += (ord(hexval[i]) - 55) * base
            base = base * 16
 
    return dec_val

def bigToHex(value,size):
    hexaDeciNum = ['0']*(size*2)
 
    i = (len(hexaDeciNum)-1)
    while(value != 0):
        temp = 0
        temp = value % 16
 
        # check if temp < 10
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i - 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i - 1
        value = int(value // 16)
 
    resultHex = "".join(hexaDeciNum)
    return resultHex



def littleToHex(value, size):
    hexaDeciNum = ['0']*(size*2)
 
    i = 0
    while(value != 0):
        temp = 0
        temp = value % 16
 
        # check if temp < 10
        if(temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        value = int(value // 16)
 
    resultHex = "".join(hexaDeciNum)
    resultHex=pad(resultHex[:2*size], size)
    return resultHex

if (len(sys.argv)==1):
    print("Print hex value")
    a=str.upper(input())
    print("Print number of bytes:")
    size = int(input())

elif (len(sys.argv)==2):
    a=str.upper(sys.argv[1])
    print("Print number of bytes:")
    size = int(input())
elif (len(sys.argv)==3):
    a=str.upper(sys.argv[1])
    size=int(sys.argv[2])   
    

a=pad(a[:2*size], size)



print(f"Value: 0x{str.lower(a)}\nNumber of bytes: {size}\nLittle-endian: {hexToLittle(a)}\nBig-endian: {hexToBig(a)}")
print(f"Litte to Hex:  0x{str.lower(littleToHex(hexToLittle(a),size))}\nBig to Hex:  0x{str.lower(bigToHex(hexToBig(a),size))}")

