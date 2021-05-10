class ATM(object):
    def __init__(self,cardNum, pinNum, balance):
        self.cardNum = cardNum
        self.pinNum = pinNum
        self.balance = balance
    def cashWithdrawal(self,balance):
        self.balance = balance-100
    def balanceEnquiry(self,balance):
        print(balance)
    

