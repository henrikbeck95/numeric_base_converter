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
    
    def convertFromBaseHigherToBaseLower(self, numberAux):
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
    
    def convertFromBaseLowerToBaseHigher(self, numberAux):
        print(numberAux)
        aux = 0
        amount = 0

        for i in range(len(self.array)):
            aux = self.array[i] * (self.numberBaseCurrent ** i)
            amount += aux
            print(f"{self.array[i]} * {self.numberBaseCurrent} ^ {i} = {aux}")
        
        return amount

    def convertArrayWithLettersToNumbers(arrayAux):
        print("ERROR!")
        i = 0

        #Search each element in list to replace the letter to number value
        while i < len(arrayAux):
            if arrayAux[i] == "A": arrayAux[i] = "10"
            elif arrayAux[i] == "B": arrayAux[i] = "11"
            elif arrayAux[i] == "C": arrayAux[i] = "12"
            elif arrayAux[i] == "D": arrayAux[i] = "13"
            elif arrayAux[i] == "E": arrayAux[i] = "14"
            elif arrayAux[i] == "F": arrayAux[i] = "15"
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
            i += 1
        
        print(f"\nAfter: {arrayAux}")
        return arrayAux