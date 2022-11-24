import re
def splitcode(nama_file):

    oprt1 = ['=', '!=', '==', '===', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\)', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', 'else', 'while', 'break', 'continue', 'return', r'\(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var', '&&', r'\|\|']
    oprt2 = ['=', '!=', '==', '===', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', ')', 'true', 'false', '{', '}', '[', ']', 'for', 'else', 'while', 'break', 'continue', 'return', '(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var' , '&&', '||']

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
    hasil_selanjutnya = []
    idx = 0
    while(idx!=len(hasil)):
        if(hasil[idx]=='/' and hasil[idx+1]=='/'):
            while(hasil[idx]!='\n'):
                idx+=1
        hasil_selanjutnya.append(hasil[idx])
        idx+=1
    hasil_akhir = []
    for i in range(len(hasil_selanjutnya)):
        if(hasil_selanjutnya[i]=='\n'):
            continue
        else:
            hasil_akhir.append(hasil_selanjutnya[i])
    hasil_final = []
    for i in range(len(hasil_akhir)):
        if(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt2) or (hasil_akhir[i+1] in oprt2))):
            continue
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt2) and (hasil_akhir[i+1] in oprt2))):
            continue
        else:
            hasil_final.append(hasil_akhir[i])
    return hasil_final
y = splitcode('D:\\python\\Tubes TBFO\\Tubes-TBFO\\test.txt')
print(y)