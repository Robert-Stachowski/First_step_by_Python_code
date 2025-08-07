class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount            
            return True
        else:
            return None   
   
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount                        
            return True          
        else:            
            return None            

    def get_balance(self):
        return self.__balance
    
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: podaj cyfrę")

account = BankAccount("Jan Nowak", 1000)


while True:
    menu_amount = input("Wpisz polecenie (wplata / wyplata / wyjscie): ")
    if menu_amount == "wyjscie" :
        break

    elif menu_amount == "wyplata" :        
        output_amount = get_float_input(f"Podaj kwotę wypłaty, mniejszą niż saldo( {account.get_balance()} ): ")       
        new_account = account.withdraw(output_amount)
        
        if new_account is None:
            print("---")
            print("Poucinam paluszki ;P ")
            print("---")
        else:
            print(f"Saldo po wypłacie wynosi: {new_account} ")            

    elif menu_amount == "wplata":        
        output_amount = get_float_input("Podaj kwotę wpłaty : ")
        new_account = account.deposit(output_amount)

        if new_account is None:
            print("Nie można wpłacać ujemnych kwot, zera również...")
        else:
            print(f"Saldo po wpłacie: {new_account}")

    else: 
        print("Halo, halo co tu się dzieje?")
        break
