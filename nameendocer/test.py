#!/usr/bin/env python2

def encode(num):
    x = len(str(num))
    if x >= 10:
        name = ''
        for i in range(len(str(x))):
            name = name + '1'
        name = '9' + name + '0' + str(x) + str(num)
    else:
        name = str(x) + str(num)
    return name

def decode(name):
    if len(name) > 10:
        length = 1
        while(name[length]=='1'):
            length += 1
        num = int(name[(length-1)*2+2:])
    else:
        num = int(name[1:])
    return num

if __name__ == '__main__':
    num = input()
    name = encode(num)
    print name
    print type(name)
    number = decode(name)
    print number
    print type(number)

