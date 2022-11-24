import CFGtoCNF
import CYK as cyk
import splitcode as splt
import sys

print("Sedang mengubah grammar menjadi dictionary: ")
print("Loading...")
cnfGrammar1 = CFGtoCNF.convertCFG()
filename = input("Masukkan nama file yang ingin diuji: ")
output = splt.splitcode(filename)
cyk.Cyk(output, cnfGrammar1)
