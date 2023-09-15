#!/bin/python3

buf = b"A" * 2000

try:
    print("[*] Created Fuzzing File")
    f = open("fuzz.txt","wb")

    f.write(buf)

    f.close()

except:
    print("[!] Error")
