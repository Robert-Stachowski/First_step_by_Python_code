class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount            
            return self.__balance
        else:
            return None   
   
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount                        
            return self.__balance            
        else:            
            return None
            

    def get_balance(self):
        return self.__balance

account = BankAccount("Jan Nowak", 1000)


while True:
    menu_amount = input("Wpisz polecenie (wplata / wyplata / wyjscie): ")
    if menu_amount == "wyjscie" :
        break

    elif menu_amount == "wyplata" :
        input_amount = input(f"Podaj kwotę wypłaty, mniejszą niż saldo( {account.get_balance()} ): ")
        output_amount = float(input_amount)        
        new_account = account.withdraw(output_amount)
        
        if new_account is None:
            print("---")
            print("Poucinam paluszki ;P ")
            print("---")
        else:
            print(f"Saldo po wypłacie wynosi: {new_account} ")
            

    elif menu_amount == "wplata":
        input_amount = input("Podaj kwotę wpłaty : ")
        output_amount = float(input_amount)
        new_account = account.deposit(output_amount)

        if new_account is None:
            print("Nie można wpłacać ujemnych kwot, zera również...")
        else:
            print(f"Saldo po wpłacie: {new_account}")

    else: 
        print("Halo, halo co tu się odpierdziela?")
        break
