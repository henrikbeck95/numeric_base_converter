class Utils:
    def __init__(self, array, numberValue, numberBaseCurrent, numberBaseTarget):
        self.array = array
        self.numberValue = numberValue
        self.numberBaseCurrent = numberBaseCurrent
        self.numberBaseTarget = numberBaseTarget

    def displayAllInfo(self):
        print(f"Array:\t\t\t{self.array}")
        print(f"Número:\t\t\t{self.numberValue}")
        print(f"Base current:\t\t{self.numberBaseCurrent}")
        print(f"Base target:\t\t{self.numberBaseTarget}")
        print(f"-------------------------------------------")

    def displayResult(self, result):
        print(f"-------------------------------------------")
        print(f"Síntaxe:\t\t({self.numberValue}){self.numberBaseCurrent} = ({result}){self.numberBaseTarget}")
    
    def convertBaseMethodDivider(self, numberAux):
        arrayNormal = []
        aux = int(numberAux)
        i = 0
        rest = 0
        divisionInteger = 0

        while aux > 0:
            rest = aux % self.numberBaseTarget
            amount = rest
            arrayNormal.append(amount)
            divisionInteger = aux // self.numberBaseTarget
            aux = divisionInteger
            i += 1

            print(f"{aux} / {self.numberBaseTarget} = {amount}\tRest:\t{rest}")
        
        arrayInverted = list(reversed(arrayNormal))
        self.convertArrayWithNumbersToLetters(arrayInverted)

        return ''.join(map(str, arrayInverted))
    
    def convertBaseMethodMultiplier(self, numberAux):
        print(numberAux)
        aux = 0
        amount = 0

        for i in range(len(self.array)):
            aux = self.array[i] * (self.numberBaseCurrent ** i)
            amount += aux
            print(f"{self.array[i]} * {self.numberBaseCurrent} ^ {i} = {aux}")
        
        return amount

    def convertArrayWithLettersToNumbers(arrayAux):
        i = 0

        #Search each element in list to replace the letter to number value
        while i < len(arrayAux):
            if arrayAux[i] == "A": arrayAux[i] = "10"
            elif arrayAux[i] == "B": arrayAux[i] = "11"
            elif arrayAux[i] == "C": arrayAux[i] = "12"
            elif arrayAux[i] == "D": arrayAux[i] = "13"
            elif arrayAux[i] == "E": arrayAux[i] = "14"
            elif arrayAux[i] == "F": arrayAux[i] = "15"
            elif arrayAux[i] == "G": arrayAux[i] = 16
            elif arrayAux[i] == "H": arrayAux[i] = 17
            elif arrayAux[i] == "I": arrayAux[i] = 18
            elif arrayAux[i] == "J": arrayAux[i] = 19
            elif arrayAux[i] == "K": arrayAux[i] = 20
            elif arrayAux[i] == "L": arrayAux[i] = 21
            elif arrayAux[i] == "M": arrayAux[i] = 22
            elif arrayAux[i] == "N": arrayAux[i] = 23
            elif arrayAux[i] == "O": arrayAux[i] = 24
            elif arrayAux[i] == "P": arrayAux[i] = 25
            elif arrayAux[i] == "Q": arrayAux[i] = 26
            elif arrayAux[i] == "R": arrayAux[i] = 27
            elif arrayAux[i] == "S": arrayAux[i] = 28
            elif arrayAux[i] == "T": arrayAux[i] = 29
            elif arrayAux[i] == "U": arrayAux[i] = 30
            elif arrayAux[i] == "V": arrayAux[i] = 31
            elif arrayAux[i] == "W": arrayAux[i] = 32
            i += 1
        
        return arrayAux

    def convertArrayWithNumbersToLetters(self, arrayAux):
        print(f"\nBefore: {arrayAux}\n")

        i = 0

        #Search each element in list to replace the letter to number value
        while i < len(arrayAux):
            print(f"{i} = {arrayAux[i]}")
            if arrayAux[i] == 10: arrayAux[i] = "A"
            elif arrayAux[i] == 11: arrayAux[i] = "B"
            elif arrayAux[i] == 12: arrayAux[i] = "C"
            elif arrayAux[i] == 13: arrayAux[i] = "D"
            elif arrayAux[i] == 14: arrayAux[i] = "E"
            elif arrayAux[i] == 15: arrayAux[i] = "F"
            elif arrayAux[i] == 16: arrayAux[i] = "G"
            elif arrayAux[i] == 17: arrayAux[i] = "H"
            elif arrayAux[i] == 18: arrayAux[i] = "I"
            elif arrayAux[i] == 19: arrayAux[i] = "J"
            elif arrayAux[i] == 20: arrayAux[i] = "K"
            elif arrayAux[i] == 21: arrayAux[i] = "L"
            elif arrayAux[i] == 22: arrayAux[i] = "M"
            elif arrayAux[i] == 23: arrayAux[i] = "N"
            elif arrayAux[i] == 24: arrayAux[i] = "O"
            elif arrayAux[i] == 25: arrayAux[i] = "P"
            elif arrayAux[i] == 26: arrayAux[i] = "Q"
            elif arrayAux[i] == 27: arrayAux[i] = "R"
            elif arrayAux[i] == 28: arrayAux[i] = "S"
            elif arrayAux[i] == 29: arrayAux[i] = "T"
            elif arrayAux[i] == 30: arrayAux[i] = "U"
            elif arrayAux[i] == 31: arrayAux[i] = "V"
            elif arrayAux[i] == 32: arrayAux[i] = "W"

            i += 1
        
        print(f"\nAfter: {arrayAux}")
        return arrayAux