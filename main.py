import CFGtoCNF
import CYK as cyk
import splitcode as splt
from time import sleep


print("=================================================")
print("== Selamat datang di Command Parser Javascript ==")
print("=================================================")
sleep(1)
print("Sedang mengubah grammar menjadi dictionary: ")
print("Loading...")
sleep(1)
cnfGrammar1 = CFGtoCNF.convertCFG()
filename = input("Masukkan nama file yang ingin diuji: ")
output = splt.splitcode(filename)
# print("Output: ")
# print(output)
sleep(1)
print("Sedang mengecek sintaks...")
cyk.Cyk(output, cnfGrammar1)
