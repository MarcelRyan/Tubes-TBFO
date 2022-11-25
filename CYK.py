def Cyk(out,cnf):
    length = len(out)
    table = [[set([]) for i in range (length)] for j in range(length)]
    for i in range(length):
        for var in cnf.items():
            for trmnl in var[1]:
                if len(trmnl)==1 and trmnl[0]==out[i]:
                    table[i][i].add(var[0])

    for j in range(2,length+1):
        for k in range(0,length-j+1):
            l = j+k-1
            for a in range(k,l):
                for var in cnf.items():
                    for produc in var[1]:
                        if len(produc)==2:
                            if(produc[0] in table[k][a]) and (produc[1] in table[a+1][l]):
                                table[k][l].add(var[0])

    if "S0" in table[0][length-1]:
        print("Accepted Syntax :D")
    else:
        print("Syntax Error D:")
