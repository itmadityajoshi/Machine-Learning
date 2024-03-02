from abc import ABC, abstractmethod

class BankingApp:

    def database(Self):
        return f'database is connected'
    
    @abstractmethod
    def security(self):
        return f'security is implemented.'
    

class MobileApp(BankingApp):
    def loginApp(self):
        return f'please lgoin '
    
    
    def security(self):
        return f'security is implemented.'


if __name__ == "__main__":
    my_Bank = BankingApp()
    print(my_Bank.database())


mobile = MobileApp()
print(mobile.security())