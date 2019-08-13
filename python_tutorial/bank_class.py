class Bank:
    def __init__(self):
        self.money = 0
        print("Bank가 생성되었습니다")
    
    def deposit(self, money):
        self.money += money
        print (self.money)

wooribank = Bank() 

wooribank.deposit(100) 



