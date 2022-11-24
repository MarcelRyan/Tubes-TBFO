def state_1(char): # Start state untuk mengecek variabel valid atau tidak
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
        state = 2
    elif (ord(char) == 95 or ord(char) == 36):
        state = 15
    else:
        state = 3
    return state

def state_2(char): # final state untuk mengecek sebuah variabel valid atau tidak
    if (ord(char) == 95 or ord(char) == 36 or (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57)):
        state = 2
    else:
        state = 3
    return state

def state_15(char): # Apabila nama variabel diawali $ atau _
    if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 57)):
        state = 2
    elif (ord(char) == 95 or ord(char) == 36):
        state = 15
    else:
        state = 3
    return state


def state_3(char): # dead state apabila variabel sudah tidak valid
    state = 3
    return state

def state_4(char): # Start state untuk mengecek apakah sebuah value valid atau tidak
    if (ord(char) >= 48 and ord(char) <= 57):
        state = 5
    elif (ord(char) == 45):
        state = 14
    else:
        state = 6
    return state
    
def state_14(char):
    if (ord(char) >= 48 and ord(char) <= 57):
        state = 5
    else:
        state = 6
    return state

def state_5(char): # Final state untuk mengecek apakah sebuah value valid atau tidak
    if (ord(char) >= 48 and ord(char) <= 57):
        state = 5
    else:
        state = 6
    return state

def state_6(char): # Dead state apabila value sudah pasti tidak valid
    state = 6
    return state

def state_7(char): # Start state untuk mengecek apakah sebuah operator valid atau tidak
    if ((ord(char) == 45) or (ord(char) == 43) or (ord(char) == 47) or (ord(char) == 37) or (ord(char) == 42) or (ord(char) == 63)):
        state = 8
    elif (ord(char) == 60 or ord(char) == 62):
        state = 9
    elif (ord(char) == 33 or ord(char) == 61):
        state = 10
    elif (ord(char) == 38):
        state = 11
    elif (ord(char) == 124):
        state = 12
    else:
        state = 13
    return state

def state_8(char): # Final state yang tidak bisa masuk ke state apapun lagi sehingga apabila masuk ke state ini operator otomatis tidak valid
    state = 13
    return state

def state_9(char): # Salah satu Final state untuk mengecek apakah sebuah operator valid atau tidak
    if (ord(char) == 61):
        state = 8
    else:
        state = 13
    return state

def state_10(char): # Salah satu Final state untuk mengecek apakah sebuah operator valid atau tidak
    if (ord(char) == 61):
        state = 9
    else:
        state = 13
    return state

def state_11(char): # Salah satu Final state untuk mengecek apakah sebuah operator valid atau tidak (untuk operator &)
    if (ord(char) == 38):
        state = 8
    else:
        state = 13
    return state

def state_12(char): # Salah satu Final state untuk mengecek apakah sebuah operator valid atau tidak (untuk operator |)
    if (ord(char) == 124):
        state = 9
    else:
        state = 13
    return state

def state_13(char): # Dead state apabila operator tidak valid
    state = 13
    return state


def VariabelValid(str): # Simulasi FA untuk mengecek apakah syntax variabel sudah valid menggunakan state 1, 2, 3
    state = 1
    for i in range(len(str)):
        if (state == 1):
            state = state_1(str[i])
        elif (state == 2):
            state = state_2(str[i])
        elif (state == 3):
            state = state_3(str[i])
        elif (state == 15):
            state = state_15(str[i])
    
    if (state == 2):
        return True
    else:
        return False

def ValueValid(str): # Simulasi FA untuk mengecek apakah syntax value sudah valid menggunakan state 4, 5, 6
    state = 4
    for i in range(len(str)):
        if (state == 4):
            state = state_4(str[i])
        elif (state == 5):
            state = state_5(str[i])
        elif (state == 6):
            state = state_6(str[i])
        elif (state == 14):
            state = state_14(str[i])
    
    if (state == 5):
        return True
    else:
        return False

def OperatorValid(str): # Simulasi FA untuk mengecek apakah syntax operator sudah valid menggunakan state 7, 8, 9, 10, 11, 12, 13
    state = 7
    for i in range(len(str)):
        if (state == 7):
            state = state_7(str[i])
        elif (state == 8):
            state = state_8(str[i])
        elif (state == 9):
            state = state_9(str[i])
        elif (state == 10):
            state = state_10(str[i])
        elif (state == 11):
            state = state_11(str[i])
        elif (state == 12):
            state = state_12(str[i])
        elif (state == 13):
            state = state_13(str[i])
    
    if (state == 8 or state == 9 or state == 10 or state == 11 or state == 12):
        return True
    else:
        return False
    

# str1 = "$$$$23"
# if (VariabelValid(str1)):
#     print("Variabel diterima")
# else:
#     print("Variabel ditolak")

# str2 = "-13"
# if (ValueValid(str2)):
#     print("Value diterima")
# else:
#     print("Value tidak diterima")

# str3 = ">="
# if (OperatorValid(str3)):
#     print("Operator valid")
# else:
#     print("Operator tidak valid")