#! /usr/bin/python3

import os

def sh(code):
	os.system(code)

for i in os.listdir():
    if i.endswith(".s"):
        print(i)
        sh(f"python3 ../assembler/assembler.py {i} exec/{i.split('.s')[0] + '.out'}")

