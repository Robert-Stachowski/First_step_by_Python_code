# InputBankAccount.py

Opis projektu:  

Ten skrypt to moja pierwsza implementacja klasy BankAccount w Pythonie. Program umożliwia użytkownikowi wprowadzanie danych z klawiatury (input), wykonywanie operacji wpłaty i wypłaty oraz sprawdzanie aktualnego salda.

To jedno z moich pierwszych "większych" zadań w ramach mentoringu, mające na celu praktyczne zastosowanie programowania obiektowego (OOP). Bazowy plik nie zawierał żadnych inputów ani interakcji z użytkownikiem – ta część została dodana jako moja własna inwencja twórcza. Dodatkowo wprowadziłem podstawową obsługę błędów, która zapobiega wpisywaniu nieprawidłowych danych (np. liter zamiast liczb).


---

Czego się tutaj uczę:

- Tworzenia klas i obiektów
- Definiowania metod (deposit, withdraw)
- Użycia pętli while do interakcji z użytkownikiem
- Obsługi danych wejściowych z klawiatury
- Warunków if/else
- Obsługi błędów i niepoprawnych danych
- Podstaw dobrej struktury kodu

---

Jak uruchomić:

python InputBankAccount.py

Upewnij się, że masz zainstalowanego Pythona 3.10+.

---

Zawartość pliku:

- class BankAccount: – klasa reprezentująca konto bankowe
- deposit(self, amount) – metoda do wpłacania środków
- withdraw(self, amount) – metoda do wypłacania środków z uwzględnieniem limitów
- while True: – pętla pobierająca dane od użytkownika
- Warunki i obsługa błędów (np. ValueError)

---

Dodatkowo:

Ten plik powstał jako część mojego rozwoju w ramach nauki Pythona od podstaw. Początkowo był użyty również w pull requeście do repozytorium mentora. Tutaj został uporządkowany jako element osobistego portfolio i wzbogacony o własne rozszerzenia.

---

Autor:

Robert Stachowski  
Mentoring Python | Poziom: podstawy / OOP  
Repozytorium: https://github.com/Robert-Stachowski/First_step_by_Python_code
