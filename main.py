import CFGtoCNF
import CYK as cyk
import sys
import splitcode as splt
import dummyCYK
import splitdummy
import dummyCNF


cnfGrammar1 = CFGtoCNF.convertCFG()
print("ini Key 1: ")
print(cnfGrammar1.keys())
print("Ini value 1: ")
print(cnfGrammar1.values())


filename = input("Masukkan nama file: ")
output = splt.splitcode(filename)
cyk.Cyk(output, cnfGrammar1)
