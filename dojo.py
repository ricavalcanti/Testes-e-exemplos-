def nRomanos(numero):
    romanos = ((1,'I'),(5,'V'),(10,'X'))
    revRomanos = tuple(reversed(romanos))
    nInRoman = ''
    index = 0
    while (numero>0):
        multiplo = numero // revRomanos[index][0]
        # import pdb; pdb.set_trace()
        if multiplo!=0:
            nInRoman = nInRoman + multiplo * revRomanos[index][1]
            numero = numero % revRomanos[index][0]
        index = index + 1

    return nInRoman
    
print(nRomanos(6))