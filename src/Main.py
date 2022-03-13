from Utils import Utils

class Main:
    def __init__(self, numberValue, numberBaseCurrent, numberBaseTarget):
        self.numberValue = str(numberValue)
        self.numberBaseCurrent = numberBaseCurrent
        self.numberBaseTarget = numberBaseTarget

        #Split each digit into a different index inside array
        self.arrayStringNormal = list(self.numberValue)
        self.arrayStringNormal = self.convertArrayWithLettersToNumbers()
        self.arrayNumberNormal = [ int(x) for x in self.arrayStringNormal ]
        self.arrayStringInverted = list(reversed(self.arrayStringNormal))
        self.arrayNumberInverted = [ int(x) for x in self.arrayStringInverted ]

        #print(f"{self.arrayStringNormal}")
        #print(f"{self.arrayNumberNormal}")
        #print(f"{self.arrayStringInverted}")
        #print(f"{self.arrayNumberInverted}")
        
        #self.numberValue = int(self.numberValue)
        self.numberValue = self.numberValue
        #print(f"{self.numberValue}")

        #Utils.convertArrayWithLettersToNumbers()

    def convertArrayWithLettersToNumbers(self):
        i = 0

        #Search each element in list to replace the letter to number value
        while i < len(self.arrayStringNormal):
            if self.arrayStringNormal[i] == "A": self.arrayStringNormal[i] = "10"
            elif self.arrayStringNormal[i] == "B": self.arrayStringNormal[i] = "11"
            elif self.arrayStringNormal[i] == "C": self.arrayStringNormal[i] = "12"
            elif self.arrayStringNormal[i] == "D": self.arrayStringNormal[i] = "13"
            elif self.arrayStringNormal[i] == "E": self.arrayStringNormal[i] = "14"
            elif self.arrayStringNormal[i] == "F": self.arrayStringNormal[i] = "15"
            i += 1
        
        return self.arrayStringNormal

    def selectWorkflow(self):
        callingUtils = Utils(self.arrayNumberInverted, self.numberValue, self.numberBaseCurrent, self.numberBaseTarget)
        
        callingUtils.displayAllInfo()

        #Choosing methods workflow
        if self.numberBaseCurrent > 10:
            print("Funcionando por aqui")
            result = callingUtils.convertFromBaseLowerToBaseHigher(self.arrayNumberNormal)
        elif self.numberBaseTarget > 10:
            print("Arrumando aqui")
            result = callingUtils.convertFromBaseHigherToBaseLower(self.numberValue)
        else:
            #Decision structure calculation workflow
            if self.numberBaseCurrent == self.numberBaseTarget:
                result = self.numberValue
            elif self.numberBaseCurrent <= self.numberBaseTarget:
                result = callingUtils.convertFromBaseLowerToBaseHigher(self.numberValue)
            elif self.numberBaseCurrent >= self.numberBaseTarget:
                result = callingUtils.convertFromBaseHigherToBaseLower(self.numberValue)

        #Display results
        callingUtils.displayResult(result)
        return result

callingMain = Main("1FA", 16, 8) #506
callingMain.selectWorkflow()
#result = callingMain.selectWorkflow()
#print(result)