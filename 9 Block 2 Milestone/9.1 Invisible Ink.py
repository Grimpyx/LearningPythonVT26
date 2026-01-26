def bin2dec(bin):
    dec = 0
    for i in range(len(bin)):
        exponent = len(bin) - i - 1
        dec += (2**exponent) * int(bin[i])
    return dec

def dec2bin(dec):
    bin = ""
    while dec > 0:
        # As shown in the slides
        #bit_str = str(dec % 2)
        #bin_str = bit_str + bin_str
        #dec = dec // 2

        # Compact and very cool way where we use bitwise operators!
        bin = str(dec & 1) + bin # "grabs" the first bit by, basically a logical and on the first bit. Convert to string, put in front.
        dec >>= 1 # Shift everything to the right one step. Then we repeat.
    return bin

def padzero(bin, n):
    need = n - len(bin)
    bin = need * '0' + bin
    return bin

def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(padzero(dec2bin(ord(c)),8))
    return "".join(bin)

def bin2txt(bin):
    txt = ""
    while len(bin) > 0:
        next8 = bin[:8]
        bin = bin[8:]

        txt = txt + chr(bin2dec(next8))
    return txt

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('	')
    return "".join(inv)

def invisible2bin(inv):
    bin = ""
    for c in inv:
        bin = bin + str(int(c != ' '))
    return bin

def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))

def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))

# prints "just testing this and see if I get the same result from my algorithm 1234567890"
print(invisible2txt(" \t\t \t \t  \t\t\t \t \t \t\t\t  \t\t \t\t\t \t    \t      \t\t\t \t   \t\t  \t \t \t\t\t  \t\t \t\t\t \t   \t\t \t  \t \t\t \t\t\t  \t\t  \t\t\t  \t      \t\t\t \t   \t\t \t    \t\t \t  \t \t\t\t  \t\t  \t      \t\t    \t \t\t \t\t\t  \t\t  \t    \t      \t\t\t  \t\t \t\t  \t \t \t\t  \t \t  \t      \t\t \t  \t \t\t  \t\t   \t      \t  \t  \t  \t      \t\t  \t\t\t \t\t  \t \t \t\t\t \t    \t      \t\t\t \t   \t\t \t    \t\t  \t \t  \t      \t\t\t  \t\t \t\t    \t \t\t \t\t \t \t\t  \t \t  \t      \t\t\t  \t  \t\t  \t \t \t\t\t  \t\t \t\t\t \t \t \t\t \t\t   \t\t\t \t    \t      \t\t  \t\t  \t\t\t  \t  \t\t \t\t\t\t \t\t \t\t \t  \t      \t\t \t\t \t \t\t\t\t  \t  \t      \t\t    \t \t\t \t\t   \t\t  \t\t\t \t\t \t\t\t\t \t\t\t  \t  \t\t \t  \t \t\t\t \t   \t\t \t    \t\t \t\t \t  \t       \t\t   \t  \t\t  \t   \t\t  \t\t  \t\t \t    \t\t \t \t  \t\t \t\t   \t\t \t\t\t  \t\t\t     \t\t\t  \t  \t\t    "))
