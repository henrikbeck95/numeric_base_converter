from Utils import Utils

class Main:
    def __init__(self, numberValue, numberBaseCurrent, numberBaseTarget):
        self.numberValue = str(numberValue)
        self.numberBaseCurrent = numberBaseCurrent
        self.numberBaseTarget = numberBaseTarget

        #Split each digit into a different index inside array
        self.arrayStringNormal = list(self.numberValue)
        self.arrayStringNormal = Utils.convertArrayWithLettersToNumbers(self.arrayStringNormal)
        self.arrayNumberNormal = [ int(x) for x in self.arrayStringNormal ]
        self.arrayStringInverted = list(reversed(self.arrayStringNormal))
        self.arrayNumberInverted = [ int(x) for x in self.arrayStringInverted ]
        
        #self.numberValue = int(self.numberValue)
        self.numberValue = self.numberValue

    def selectWorkflow(self):
        callingUtils = Utils(self.arrayNumberInverted, self.numberValue, self.numberBaseCurrent, self.numberBaseTarget)
        
        callingUtils.displayAllInfo()

        #Decision structure calculation workflow
        if self.numberBaseCurrent == self.numberBaseTarget:
            result = self.numberValue
        elif self.numberBaseCurrent > 10:
            result = callingUtils.convertFromBaseLowerToBaseHigher(self.arrayNumberNormal)
        elif self.numberBaseTarget > 10:
            result = callingUtils.convertFromBaseHigherToBaseLower(self.numberValue)
        else:
            if self.numberBaseCurrent <= self.numberBaseTarget:
                result = callingUtils.convertFromBaseLowerToBaseHigher(self.numberValue)
            elif self.numberBaseCurrent >= self.numberBaseTarget:
                result = callingUtils.convertFromBaseHigherToBaseLower(self.numberValue)

        #Display results
        callingUtils.displayResult(result)
        return result

#Declaring the global variables
#numberValue = input("Valor numérico: ")
#numberBaseCurrent = input("Base numérica atual: ")
#numberBaseTarget = input("Base numérica desejada: ")
numberValue = 127
numberBaseCurrent = 10
numberBaseTarget = 8

#Calculate the operation
callingMain = Main(numberValue, numberBaseCurrent, numberBaseTarget)
callingMain.selectWorkflow()