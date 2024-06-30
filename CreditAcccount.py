from SavingsAccount import SavingsAccount
class CreditAccount(SavingsAccount):

    def withdraw(self, amount, passkey):
        if self.checkPasskey(passkey):
            self._balance -= amount
            return "Success"
        else:
            return "Invalid Passkey"


if __name__ == '__main__':
    print("Credit Account Test")
    credit = CreditAccount("Credit", 1234)
    credit.setRate(0.20)
    credit.withdraw(50, 1234)
    credit.printInfo()
    credit.applyInterest()
    credit.printInfo()
