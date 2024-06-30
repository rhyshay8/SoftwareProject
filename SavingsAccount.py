from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def setRate(self, interestRate):
        self.__rate = interestRate

    def getRate (self):
        return self.__rate

    def applyInterest(self):
        self._balance += self._balance*self.__rate
    
    def printInfo(self):
        # Account <name> has a balance of $<x>
        print("Account {} has a balance of ${} with rate of {}".format(self.getName(), self.getBalance(), self.__rate))


if __name__ == '__main__':
    print("Savings Account Test")
    savings = SavingsAccount("Savings", 1234)
    savings.deposit(100)
    savings.setRate(0.05)
    savings.applyInterest()
    savings.printInfo()
