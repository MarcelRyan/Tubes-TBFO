import re
def splitcode(nama_file):

    oprt1 = ['=', '!=', '!', '==', '===', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\)', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', 'else', 'while', 'break', 'continue', 'return', r'\(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var', '&&', r'\|\|', 'except', r'\?']
    oprt2 = ['=', '!=', '!', '==', '===', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', ')', 'true', 'false', '{', '}', '[', ']', 'for', 'else', 'while', 'break', 'continue', 'return', '(', 'function', 'let', 'if', ';', 'const', 'case', 'catch', 'default', 'delete', 'finally', 'null', 'return', 'switch', 'throw', 'try', 'var' , '&&', '||', 'except', '?']
    variabel = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    oprt3 = ['=', '>', '<', '!', '+', '-', '\\', '/', '*', '%', '&', '|']
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
            if (stmnt2 == 'await' or stmnt2 == 'of'  or stmnt2 == 'in' or stmnt2 == 'if' or stmnt2 == '&&' or stmnt2 == '||' or stmnt2=='let' or stmnt2=='delete'):
                hasil.append(stmnt2)
            else:
                split = list(stmnt2)
                hasil.extend(split)
    hasil_selanjutnya1 = []
    komen = 0
    while(komen!=len(hasil)):
        if(komen+1!=len(hasil) and hasil[komen]=='/' and hasil[komen+1]=='*'):
            j = komen
            hasil_selanjutnya1.append(hasil[j])
            hasil_selanjutnya1.append(hasil[j+1])
            while(komen<len(hasil) and (hasil[komen]!='*' or hasil[komen+1]!='/')):
                    komen+=1
        if(komen>=len(hasil)):
            break
        else:
            hasil_selanjutnya1.append(hasil[komen])
            komen+=1


    hasil_selanjutnya = []
    idx = 0
    while(idx<len(hasil_selanjutnya1)):#buat menghilangkan komen //
        if(idx+1!=len(hasil_selanjutnya1) and hasil_selanjutnya1[idx]=='/' and hasil_selanjutnya1[idx+1]=='/'):
            while(hasil_selanjutnya1[idx]!='\n' and idx<len(hasil_selanjutnya1)-1):
                idx+=1
            if(idx>=len(hasil_selanjutnya1)-1):
                break
        hasil_selanjutnya.append(hasil_selanjutnya1[idx])
        idx+=1
    hasil_akhir = []
    for i in range(len(hasil_selanjutnya)):
        if(hasil_selanjutnya[i]=='\n'):
            continue
        else:
            hasil_akhir.append(hasil_selanjutnya[i])
    hasil_final = []
    for i in range(len(hasil_akhir)):
        if(hasil_akhir[i]==' ' and i==(len(hasil_akhir)-1)):
            continue
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt3) and (hasil_akhir[i+1] in oprt3))):
            hasil_final.append(hasil_akhir[i])
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in variabel) and (hasil_akhir[i+1] in variabel))):
            hasil_final.append(hasil_akhir[i])
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt3) or (hasil_akhir[i+1] in oprt3))):
            continue
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in variabel) or (hasil_akhir[i+1] in variabel))):
            continue
        elif(hasil_akhir[i]==' ' and ((hasil_akhir[i-1] in oprt2) or (hasil_akhir[i+1] in oprt2))):
            continue
        else:
            hasil_final.append(hasil_akhir[i])
    i = 0
    while (i < len(hasil_final)-5):
        if (hasil_final[i] == 'd' and hasil_final[i+1] == 'e' and hasil_final[i+2] == 'let' and hasil_final[i+3] == 'e' and hasil_final[i+4] == ' '): # Kalau delete sintaks dari javascript
            hasil_final.pop(i)
            hasil_final.pop(i)
            hasil_final.pop(i)
            hasil_final.pop(i)
            hasil_final.pop(i)
            hasil_final.insert(i, 'delete')
            i -= 4
        elif (hasil_final[i] == 'd' and hasil_final[i+1] == 'e' and hasil_final[i+2] == 'let' and hasil_final[i+3] == 'e'): # Kalau delete berupa string bukan sintaks dari javascript
            hasil_final.pop(i+2)
            hasil_final.insert(i+2, 't')
            hasil_final.insert(i+2, 'e')
            hasil_final.insert(i+2, 'l')
            i += 2
        i += 1
    return hasil_final

# y = splitcode('D:\\python\\Tubes TBFO\\Tubes-TBFO\\coab.txt')
# print(y)
