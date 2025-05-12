class Bank:

    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

acc1 = Bank("Adeel")
acc2 = Bank("Ahmed") 

acc1.display_info()
acc2.display_info()

Bank.change_bank_name("Habib Bank")

acc1.display_info()
acc2.display_info()