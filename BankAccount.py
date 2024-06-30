class BankAccount:
    def __init__(self, name, passkey):
        self.__name = name
        self.__passkey = passkey
        self._balance = 0


    def getBalance(self):
        return self._balance
    
    def getName (self):
        return self.__name
    
    def deposit(self, amount):
        self._balance += amount
    def printInfo(self):
        # Account <name> has a balance of $<x>
        print("Account {} has a balance of ${}".format(self.__name, self._balance))
    
    def withdraw(self, amount, passkey):
        if passkey != self.__passkey:
            return "Invalid Passkey"
        if amount > self._balance:
            return "Insufficient Funds"
        
        self.__balance -= amount
        return "Success"
    
    def checkPasskey(self, passkey):
        return passkey == self.__passkey
    
if __name__ == '__main__':
    print("Bank Account Test")
    account = BankAccount("Savings", 1234)
    account.printInfo()


