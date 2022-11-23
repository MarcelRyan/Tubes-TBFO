import CFGtoCNF
import CYK as cyk
import splitcode as splt


cnfGrammar1 = CFGtoCNF.convertCFG()


filename = 'test.txt'
output = splt.splitcode(filename)
print(output)
cyk.Cyk(output, cnfGrammar1)
