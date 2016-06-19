# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/env python
import Image
import re



file = open(r"stego100.txt")
num = 0;
for f in file:
    num = num + 1;

for t in range(2,num):
    if num % t == 0:
        i = t;
        j = num / i
        file = open(r"stego100.txt")
        pic = Image.new("RGB",(i, j))
        print i , j
        for w in range(0,i):
            for h in range(0,j):
                linec = file.readline()
                linenums =  re.findall(r'([0-9]+)',linec);
                r = int(linenums[0])
                g = int(linenums[1])
                b = int(linenums[2])
                pic.putpixel([w,h],(r,g,b))
               # print r,g,b
        pic.save(str(i)+"i.png")
        print i


