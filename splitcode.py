import re
def splitcode(nama_file):

    oprt1 = ['=', '!=', '==', '===', '>=', '<=', '<', '>', ':'',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\)', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', 'else', 'while', 'break', 'continue', 'return', r'\(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var', '&&', r'\|\|']
    oprt2 = ['=', '!=', '==', '===', '>=', '<=', '<', '>', ':'',', '/', '-', '+', '*', '**', "'", '"', ')', 'true', 'false', '{', '}', '[', ']', 'for', 'else', 'while', 'break', 'continue', 'return', '(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var' , '&&', '||']

    file = open(nama_file,"r")
    isi  = file.read()
    file.close()
    isi = isi.split('  ')       
    # re.split(r'\s+',isi)
    for oprt in oprt1:
        hasil = []
        for stmnt in isi:
            elmnt = re.split(r'[A..z]*(' + oprt + r')[A..z]*', stmnt)
            for split in elmnt:
                hasil.append(split)
        isi = hasil

    hasil = []
    for stmnt2 in isi:
        if(stmnt2 in oprt2):
            hasil.append(stmnt2)
        else:
            if (stmnt2 == 'await' or stmnt2 == 'of'  or stmnt2 == 'in' or stmnt2 == 'if' or stmnt2 == '&&' or stmnt2 == '||'):
                hasil.append(stmnt2)
            else:
                split = list(stmnt2)
                hasil.extend(split)
    hasil_akhir = []
    for i in range(len(hasil)):
        if(hasil[i]=='\n'):
            continue
        else:
            hasil_akhir.append(hasil[i])
    hasil_final = []
    for i in range(len(hasil_akhir)):
        if(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt1) or (hasil_akhir[i+1] in oprt1))):
            continue
        else:
            hasil_final.append(hasil_akhir[i])
    return hasil_final
#y = splitcode('D:\python file\TBFO\js.txt')
#print(y)