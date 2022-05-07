import os

#from Utils import Utils
from Calculator import Calculator

def clear():
    #Clear terminal prompt screen according to operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def isInteger(string):
    if string[0] == ('-', '+'):
        return string[1:].isdigit()
    else:
        return string.isdigit()

clear()

while True:
    #Menu option list
    print("[1] Converter número decimal para base binária")
    print("[2] Converter número decimal para base octal")
    print("[3] Converter número decimal para base hexadecimal")
    print("[4] Converter base binária para decimal")
    print("[5] Converter base octal para decimal")
    print("[6] Converter base hexadecimal para decimal")
    print("[0] Sair")

    #Menu selected option by user
    menuOption = input("Informe a opção desejada: ")

    #Menu selected option validation for not breaking the software
    if isInteger(menuOption) == True:
        menuOption = int(menuOption)
    else:
        menuOption == 99

    #Menu workflow according the selected option
    if menuOption == 0:
        break
    elif menuOption == 1:
        numberBaseCurrent = 10
        numberBaseTarget = 2
        numberValue = input("Informe número a ser convertido: ")
    elif menuOption == 2:
        numberBaseCurrent = 10
        numberBaseTarget = 8
        numberValue = input("Informe número a ser convertido: ")
    elif menuOption == 3:
        numberBaseCurrent = 10
        numberBaseTarget = 16
        numberValue = input("Informe número a ser convertido: ")
    elif menuOption == 4:
        numberBaseCurrent = 2
        numberBaseTarget = 10
        numberValue = input("Informe número a ser convertido: ")
    elif menuOption == 5:
        numberBaseCurrent = 8
        numberBaseTarget = 10
        numberValue = input("Informe número a ser convertido: ")
    elif menuOption == 6:
        numberBaseCurrent = 16
        numberBaseTarget = 10
        numberValue = input("Informe número a ser convertido: ")
    else:
        print("A opção selecionada é inválida!")
        print("Para não perder a viagem até aqui, demonstraremos a seguir a comprovação que (0)x = (0)y para qualquer base decimal")
        
        numberBaseCurrent = 0
        numberBaseTarget = 0
        numberValue = 0

    #Calculate
    callingCalculator = Calculator(numberValue, numberBaseCurrent, numberBaseTarget)
    callingCalculator.selectWorkflow()

    input("Pressione a tecla ENTER para continuar...")
    clear()

###########################################################
#Testing section
###########################################################

#Declaring the global variables (by input method)
#numberValue = input("Valor numérico: ") #Letters must be set as uppercase
#numberBaseCurrent = int(input("Base numérica atual: "))
#numberBaseTarget = int(input("Base numérica desejada: "))

#Declaring the global variables (by set value)
#numberValue = 127
#numberBaseCurrent = 10
#numberBaseTarget = 8

#Calculate the operation
#callingCalculator = Calculator(numberValue, numberBaseCurrent, numberBaseTarget)

###########################################################
#Testing values section - begin
#This section can be removed later
#
#Passed equal numeric base
#callingCalculator = Calculator(3748, 10, 10) #3748
#callingCalculator = Calculator(1977, 10, 10) #1977
#callingCalculator = Calculator(2345, 10, 10) #2345
#callingCalculator = Calculator(129, 10, 10) #129
#callingCalculator = Calculator(4379, 10, 10) #4379
#
#Passed diff numeric base (proof)
#callingCalculator = Calculator(257, 8, 10) #175
#callingCalculator = Calculator(2345, 8, 10) #1253
#callingCalculator = Calculator(720, 8, 10) #464
#callingCalculator = Calculator(6132, 8, 10) #3162
#callingCalculator = Calculator(126, 8, 10) #86
#callingCalculator = Calculator(4370, 8, 10) #2296
#callingCalculator = Calculator(542, 8, 10) #354
#callingCalculator = Calculator(27, 8, 2) #11011
#callingCalculator = Calculator(23, 8, 2) #10111
#callingCalculator = Calculator(10, 2, 10) #2
#callingCalculator = Calculator(11101, 2, 10) #29
#callingCalculator = Calculator(1011, 2, 10) #11
#callingCalculator = Calculator(11011, 2, 10) #27
#callingCalculator = Calculator(111111, 2, 10) #63
#callingCalculator = Calculator(100110, 2, 10) #38
#callingCalculator = Calculator(177, 10, 8) #261
#callingCalculator = Calculator("1FA", 16, 8) #506
#callingCalculator = Calculator(685, 10, 16) #2AD
#
#Passed diff numeric base (counter-proof)
#callingCalculator = Calculator(175, 10, 8) #257
#callingCalculator = Calculator(1253, 10, 8) #2345
#callingCalculator = Calculator(464, 10, 8) #720
#callingCalculator = Calculator(3162, 10, 8) #6132
#callingCalculator = Calculator(86, 10, 8) #126
#callingCalculator = Calculator(2296, 10, 8) #4370
#callingCalculator = Calculator(354, 10, 8) #542
#callingCalculator = Calculator(11011, 2, 8) #27
#callingCalculator = Calculator(10111, 2, 8) #23
#callingCalculator = Calculator(2, 10, 2) #10
#callingCalculator = Calculator(29, 10, 2) #11101
#callingCalculator = Calculator(11, 10, 2) #1011
#callingCalculator = Calculator(27, 10, 2) #11011
#callingCalculator = Calculator(63, 10, 2) #111111
#callingCalculator = Calculator(38, 10, 2) #100110
#callingCalculator = Calculator(261, 8, 10) #177
#callingCalculator = Calculator(506, 8, 16) #1FA
#callingCalculator = Calculator("2AD", 16, 10) #685
#
#Error
#callingCalculator = Calculator(542, 8, 16) #162
#callingCalculator = Calculator("1E", 16, 2) #11110
#callingCalculator = Calculator(11110, 2, 16) #1E
#
#Testing values section - end
###########################################################

#Essential to work (not part of testing section)
#callingCalculator.selectWorkflow()