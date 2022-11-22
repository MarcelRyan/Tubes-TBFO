import json
import sys
variablesJar = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1",
"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2", "K2", "L2", "M2", "N2", "O2", "P2", "Q2", "R2", "S2", "T2", "U2", "V2", "W2", "X2", "Y2", "Z2",
"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3", "K3", "L3", "M3", "N3", "O3", "P3", "Q3", "R3", "S3", "T3", "U3", "V3", "W3", "X3", "Y3", "Z3",
"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4", "K4", "L4", "M4", "N4", "O4", "P4", "Q4", "R4", "S4", "T4", "U4", "V4", "W4", "X4", "Y4", "Z4",
"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5",
"A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6", "K6", "L6", "M6", "N6", "O6", "P6", "Q6", "R6", "S6", "T6", "U6", "V6", "W6", "X6", "Y6", "Z6",
"A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7", "K7", "L7", "M7", "N7", "O7", "P7", "Q7", "R7", "S7", "T7", "U7", "V7", "W7", "X7", "Y7", "Z7",
"A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8", "K8", "L8", "M8", "N8", "O8", "P8", "Q8", "R8", "S8", "T8", "U8", "V8", "W8", "X8", "Y8", "Z8",
"A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9", "K9", "L9", "M9", "N9", "O9", "P9", "Q9", "R9", "S9", "T9", "U9", "V9", "W9", "X9", "Y9", "Z9",
"A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", "I10", "J10", "K10", "L10", "M10", "N10", "O10", "P10", "Q10", "R10", "S10", "T10", "U10", "V10", "W10", "X10", "Y10", "Z10",
"A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11", "I11", "J11", "K11", "L11", "M11", "N11", "O11", "P11", "Q11", "R11", "S11", "T11", "U11", "V11", "W11", "X11", "Y11", "Z11",
"A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12", "I12", "J12", "K12", "L12", "M12", "N12", "O12", "P12", "Q12", "R12", "S12", "T12", "U12", "V12", "W12", "X12", "Y12", "Z12",
"A13", "B13", "C13", "D13", "E13", "F13", "G13", "H13", "I13", "J13", "K13", "L13", "M13", "N13", "O13", "P13", "Q13", "R13", "S13", "T13", "U13", "V13", "W13", "X13", "Y13", "Z13",
"A14", "B14", "C14", "D14", "E14", "F14", "G14", "H14", "I14", "J14", "K14", "L14", "M14", "N14", "O14", "P14", "Q14", "R14", "S14", "T14", "U14", "V14", "W14", "X14", "Y14", "Z14",
"A15", "B15", "C15", "D15", "E15", "F15", "G15", "H15", "I15", "J15", "K15", "L15", "M15", "N15", "O15", "P15", "Q15", "R15", "S15", "T15", "U15", "V15", "W15", "X15", "Y15", "Z15",
"A16", "B16", "C16", "D16", "E16", "F16", "G16", "H16", "I16", "J16", "K16", "L16", "M16", "N16", "O16", "P16", "Q16", "R16", "S16", "T16", "U16", "V16", "W16", "X16", "Y16", "Z16",
"A17", "B17", "C17", "D17", "E17", "F17", "G17", "H17", "I17", "J17", "K17", "L17", "M17", "N17", "O17", "P17", "Q17", "R17", "S17", "T17", "U17", "V17", "W17", "X17", "Y17", "Z17",
"A18", "B18", "C18", "D18", "E18", "F18", "G18", "H18", "I18", "J18", "K18", "L18", "M18", "N18", "O18", "P18", "Q18", "R18", "S18", "T18", "U18", "V18", "W18", "X18", "Y18", "Z18",
"A19", "B19", "C19", "D19", "E19", "F19", "G19", "H19", "I19", "J19", "K19", "L19", "M19", "N19", "O19", "P19", "Q19", "R19", "S19", "T19", "U19", "V19", "W19", "X19", "Y19", "Z19",
"A20", "B20", "C20", "D20", "E20", "F20", "G20", "H20", "I20", "J20", "K20", "L20", "M20", "N20", "O20", "P20", "Q20", "R20", "S20", "T20", "U20", "V20", "W20", "X20", "Y20", "Z20",
"A21", "B21", "C21", "D21", "E21", "F21", "G21", "H21", "I21", "J21", "K21", "L21", "M21", "N21", "O21", "P21", "Q21", "R21", "S21", "T21", "U21", "V21", "W21", "X21", "Y21", "Z21",
"A22", "B22", "C22", "D22", "E22", "F22", "G22", "H22", "I22", "J22", "K22", "L22", "M22", "N22", "O22", "P22", "Q22", "R22", "S22", "T22", "U22", "V22", "W22", "X22", "Y22", "Z22",
"A23", "B23", "C23", "D23", "E23", "F23", "G23", "H23", "I23", "J23", "K23", "L23", "M23", "N23", "O23", "P23", "Q23", "R23", "S23", "T23", "U23", "V23", "W23", "X23", "Y23", "Z23",
"A24", "B24", "C24", "D24", "E24", "F24", "G24", "H24", "I24", "J24", "K24", "L24", "M24", "N24", "O24", "P24", "Q24", "R24", "S24", "T24", "U24", "V24", "W24", "X24", "Y24", "Z24",
"A25", "B25", "C25", "D25", "E25", "F25", "G25", "H25", "I25", "J25", "K25", "L25", "M25", "N25", "O25", "P25", "Q25", "R25", "S25", "T25", "U25", "V25", "W25", "X25", "Y25", "Z25",
"A26", "B26", "C26", "D26", "E26", "F26", "G26", "H26", "I26", "J26", "K26", "L26", "M26", "N26", "O26", "P26", "Q26", "R26", "S26", "T26", "U26", "V26", "W26", "X26", "Y26", "Z26",
"A27", "B27", "C27", "D27", "E27", "F27", "G27", "H27", "I27", "J27", "K27", "L27", "M27", "N27", "O27", "P27", "Q27", "R27", "S27", "T27", "U27", "V27", "W27", "X27", "Y27", "Z27",
"A28", "B28", "C28", "D28", "E28", "F28", "G28", "H28", "I28", "J28", "K28", "L28", "M28", "N28", "O28", "P28", "Q28", "R28", "S28", "T28", "U28", "V28", "W28", "X28", "Y28", "Z28",
"A29", "B29", "C29", "D29", "E29", "F29", "G29", "H29", "I29", "J29", "K29", "L29", "M29", "N29", "O29", "P29", "Q29", "R29", "S29", "T29", "U29", "V29", "W29", "X29", "Y29", "Z29",
"A30", "B30", "C30", "D30", "E30", "F30", "G30", "H30", "I30", "J30", "K30", "L30", "M30", "N30", "O30", "P30", "Q30", "R30", "S30", "T30", "U30", "V30", "W30", "X30", "Y30", "Z30",
"A31", "B31", "C31", "D31", "E31", "F31", "G31", "H31", "I31", "J31", "K31", "L31", "M31", "N31", "O31", "P31", "Q31", "R31", "S31", "T31", "U31", "V31", "W31", "X31", "Y31", "Z31",
"A32", "B32", "C32", "D32", "E32", "F32", "G32", "H32", "I32", "J32", "K32", "L32", "M32", "N32", "O32", "P32", "Q32", "R32", "S32", "T32", "U32", "V32", "W32", "X32", "Y32", "Z32"]


txt = '''Terminals:
( ) none , and or not true false + - * / % = < > ! is in " ' [ ] { } for : # if elif else while break continue pass def return range raise class from import as with a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 
Variables:
SS ALPHABET NUM OTHER SYNTAX ALPHANUM STRING_WORD VAR_FIRST VAR VALUE NUMBER VV BOOLEAN OP EXPRESSION RELATION STRING ARRAY DICT_CONTENT DICT COMMENT IF_HEADER IF ELIF_HEADER ELIF ELSE WHILE WHILE_HEADER FOR_HEADER FOR FOR_VAR ITERABLE ITERATE CONTINUE BREAK PASS DEF_HEADER DEF_S DEF RETURN FUNC_BODY IF_FUNC ELIF_FUNC ELSE_FUNC WHILE_FUNC FOR_FUNC WITH_FUNC ITERATE_FUNC BREAK_FUNC CONTINUE_FUNC RAISE CLASS CLASS_HEADER CLASS_S IMP_S IMPORT WITH WITH_HEADER FUNCTION TRUEX FALSEX NOTX IFS ELIFX ELSEX WHILEX BREAKX CONTINUEX DEFX RETURN RANGEX RAISES CLASSS FROMS IMPORTS ASS WITHS
Productions:
SS -> SS SS | IF | WHILE | FOR | CLASS | DEF | IMPORT | RAISE | COMMENT | BREAK | FUNCTION | CONTINUE | WITH | PASS | VAR = VV | VAR OP = VV | none;
ALPHABET -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z;
NUM -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;
OTHER -> $ | & | . | ? | @ | \ | ^ | ` | ~ | ! | # | % | ( | ) | * | + | - | , | / | : | < | = | > | [ | ] | _ | { | } | |;
SYNTAX -> none | and | or | is | in | TRUEX | FALSEX | NOTX | for | IFS | ELIFX | ELSEX | WHILEX | BREAKX | CONTINUEX | DEFX | RETURN | RANGEX | RAISES | CLASSS | FROMS | IMPORTS | ASS | WITHS | PASS;
VAR_FIRST -> ALPHABET | _;
ALPHANUM -> ALPHANUM ALPHANUM | NUM | VAR_FIRST;
VAR -> VAR_FIRST ALPHANUM | VAR_FIRST;
NUMBER -> NUMBER NUMBER | NUM;
NOTX -> not;
TRUEX -> true;
FALSEX -> false;
IFS -> if;
ELIFX -> elif;
ELSEX -> else;
BREAKX -> break;
CONTINUEX -> continue;
WHILEX -> while;
RANGEX -> range;
DEFX -> def;
RETURN -> return;
CLASSS -> class;
RAISES -> raise;
FROMS -> from;
IMPORTS -> import;
ASS -> as;
STRING_WORD -> STRING_WORD STRING_WORD | ALPHABET | NUM | OTHER | SYNTAX;
VALUE -> NUMBER | BOOLEAN | STRING | ARRAY | DICT | FUNCTION | VV OP VV | ( VV ) | none;
VV -> VV , VV | VALUE | VAR;
BOOLEAN -> BOOLEAN and BOOLEAN | BOOLEAN or BOOLEAN | NOTX BOOLEAN | VV RELATION VV | TRUEX | FALSEX | ( BOOLEAN ) | VAR | NUMBER | FUNCTION;
OP -> + | - | * | / | / / | * * | %;
EXPRESSION -> BOOLEAN | ( BOOLEAN );
RELATION -> > = | < = | = = | ! = | < | > | is | is NOTX | in | NOTX in;
STRING -> STRING STRING | " STRING_WORD " | ' STRING_WORD ';
ARRAY -> [ VV ] | [ ] | [ VV for VAR in VV ] | [ VV for VAR in RANGE ];
DICT -> { } | { DICT_CONTENT };
DICT_CONTENT -> VV : VV | DICT_CONTENT , DICT_CONTENT;
COMMENT -> " " " STRING_WORD " " " | ' ' ' STRING_WORD ' ' ';
IF_HEADER -> IFS EXPRESSION :;
IF -> IF_HEADER SS | IF ELIF | IF ELSE | IF_HEADER BREAKX | IF_HEADER CONTINUEX;
ELIF_HEADER -> ELIFX EXPRESSION :;
ELIF -> ELIF_HEADER SS | ELIF ELIF | ELIF ELSE | ELIF_HEADER BREAKX | ELIF_HEADER CONTINUEX;
ELSE -> ELSEX : SS | ELSEX : BREAKX | ELSEX : CONTINUEX;
WHILE_HEADER -> WHILEX EXPRESSION :;
WHILE -> WHILE_HEADER SS;
FOR_HEADER -> for FOR_VAR in ITERABLE :;
FOR_VAR -> VAR | VAR , FOR_VAR;
ITERABLE -> RANGEX ( VV ) | ( DICT ) | DICT | ( ARRAY ) | ARRAY | STRING | FUNCTION;
FOR -> FOR_HEADER SS;
ITERATE -> FOR_HEADER | WHILE_HEADER | FOR | WHILE;
BREAK -> ITERATE BREAKX | ITERATE BREAKX SS;
CONTINUE -> ITERATE CONTINUEX | ITERATE CONTINUEX SS;
PASS -> pass;
FUNCTION -> VAR ( VV ) | VAR ( );
DEF_HEADER -> DEFX VAR ( VV ) : | DEFX VAR ( ) :;
DEF_S -> DEF_S DEF_S | FUNC_BODY;
FUNC_BODY -> FUNC_BODY FUNC_BODY | IF_FUNC | FOR_FUNC | WHILE_FUNC | CONTINUE_FUNC | BREAK_FUNC | CLASS | DEF | VAR = VV | VAR OP = VV | IMPORT | FUNCTION | RAISE | WITH_FUNC | PASS | RETURN | COMMENT | none;
DEF -> DEF_HEADER DEF_S | DEF_HEADER FUNC_BODY;
RETURN -> RETURN BOOLEAN | RETURN VV | RETURN;
IF_FUNC -> IF_HEADER FUNC_BODY | IF_FUNC ELIF_FUNC | IF_FUNC ELSE_FUNC;
ELIF_FUNC -> ELIF_HEADER FUNC_BODY | ELIF_FUNC ELIF_FUNC | ELIF_FUNC ELSE_FUNC;
ELSE_FUNC -> ELSEX : FUNC_BODY;
FOR_FUNC -> FOR_HEADER FUNC_BODY;
WHILE_FUNC -> WHILE_HEADER FUNC_BODY;
ITERATE_FUNC -> FOR_FUNC | WHILE_FUNC | WHILE_HEADER | FOR_HEADER;
CONTINUE_FUNC -> ITERATE_FUNC CONTINUEX | ITERATE_FUNC CONTINUEX FUNC_BODY;
BREAK_FUNC -> ITERATE_FUNC BREAKX | ITERATE_FUNC BREAKX FUNC_BODY;
WITH_FUNC -> WITH_HEADER FUNC_BODY;
RAISE -> RAISES FUNCTION | RAISES ( );
CLASS_HEADER -> CLASSS VAR : | CLASSS VAR ( VV ) : | CLASSS VAR ( ) :;
CLASS_S -> CLASS_S CLASS_S | IF | WHILE | FOR | CLASS | DEF | FUNCTION | VAR = VV | VAR OP = VV | BREAK | CONTINUE | PASS | COMMENT;
CLASS -> CLASS_HEADER CLASS_S;
IMPORT -> FROMS VAR IMPORTS IMP_S | IMPORTS VAR ASS VAR | IMPORTS VAR;
IMP_S -> * | VAR ASS VAR | VAR;
WITH_HEADER -> WITHS FUNCTION ASS VAR :;
WITH -> WITH_HEADER SS;
WITHS -> with'''

x = txt.split("Variables:\n")[0].replace("Terminals:\n", "").replace("\n", "")
y = txt.split("Variables:\n")[1].split("Productions:\n")[0].replace("Productions:\n", "").replace("\n", "")
a = txt.split("Productions:\n")[1]
x = x.split(' ')
y = y.split(' ')
Prod = []
rules = a.replace('\n', '').split(";")
for rule in rules:
 left = rule.split(' -> ')[0].replace(' ','')
 right = rule.split(' -> ')[1].split(' | ')
 for terms in right:
  Prod.append((left , terms.split(' ')))
result = {}
for production in Prod:
 if production[0] in y and production[1][0] in x and len(production[1]) == 1:
  result[production[1][0]] = production[0]

dict = {'"': variablesJar.pop(), '\'': variablesJar.pop()}
Prod.append((dict['"'], ['"']))
Prod.append((dict['\''], ['\'']))
for prod in Prod:
 if prod[0] in y and prod[1][0] in x and len(prod[1]) == 1:
  dict[prod[1][0]] = variablesJar.pop()
  Prod.append((dict[prod[1][0]], [prod[1][0]]))

orig_stdout = sys.stdout
f = open('log.txt', 'w')
sys.stdout = f
json.dumps(dict)
#print("Dictionary baru")
#print(dict)
#print("Prod baru")
#print(Prod)
prodbaru = []
for prod in Prod:
	i = -1
	for rule in prod[1]:
		i += 1
		if rule in x and prod[0] != dict[rule]:
				#print("Prod sebelum diubah :", prod[1])
				prod[1].pop(i)
				prod[1].insert(i, dict[rule])
				#print(prod[1])
            
print("Terminal assigment")
print(Prod)

new_prod = []
for rules1 in Prod:
        # if ((rules1[0] in y) and rules1[1][0] in y and len(rules1[1]) == 1):
        if ((rules1[0] in y) and rules1[1][0] in y and len(rules1[1]) == 1):
            temp = rules1[1][0]
            rules1[1].pop()
            for rules2 in Prod:
                if (temp == rules2[0]):
                    rules1[1].append(rules2[1])
        new_prod.append(rules1)
print("Ini isinya")
print(new_prod)
'''new_prod = []
for rules1 in Prod:
        if ((rules1[0] in y) and rules1[1][0] in y and len(rules1[1]) == 1):
            temp = rules1[1][0]
            rules1[1].pop()
            for rules2 in Prod:
                if (temp == rules2[0]):
                    rules1[1].append(rules2[1])
        new_prod.append(rules1)'''
#print(new_prod)
#print("old prod: ")
#print(Prod)
#print("now prod")




for prod in Prod:
    for rule in prod[1]:
        if isinstance(rule, list):
            if(len(rule)>2):
                #print(rule)
                while(len(rule)>=2):
                    
                    print(rule)
                    #test_prod.append()
                    temp1 = rule.pop() #pop "A"
                    temp2 = rule.pop() #pop "B"
                    rule.append(variablesJar.pop())
                    Prod.append((rule, [temp1, temp2]))
print("new Prod")
print(Prod)
sys.stdout = orig_stdout
f.close()
#lines = ['Readme', 'How to write text files in Python']
#with open('readme.txt', 'w') as f:
   # f.writelines(Prod)

