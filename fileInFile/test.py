#!/usr/bin/env python3

with open('rf.data','rb') as f:
    fname = 1
    while(1):
        x = int.from_bytes(f.read(1), 'big')
        if x>0:
            break
        x = int.from_bytes(f.read(4), 'big')
        with open(str(fname), 'wb') as t:
            t.write(f.read(x))
            fname += 1
    
