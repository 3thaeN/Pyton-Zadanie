import json
import os

class DziennikZajec:
    def __init__(self, filename='journal.json'):
        self.filename = filename
        self.journal = self.read_journal()
    
    def read_journal(self):
        journal = []
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    journal = json.load(file)
        except FileNotFoundError:
            print("Wystąpił błąd! Nie odnaleziono pliku!")
        return journal
    
    def save_to_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.journal, file)
        except FileNotFoundError:
            print("Plik nie istnieje")
    
    def add_task(self, task):
        self.journal.append(task)
        self.save_to_file()
        print("Zadanie zapisane w pliku!")
    
    def edit_task(self, number, new_task):
        try:
            if 0 <= number < len(self.journal):
                self.journal[number] = new_task
                self.save_to_file()
                print("Zadanie zedytowane poprawnie!")
        except ValueError:
            print("Zadanie o takim numerze nie istnieje!")
    
    def remove_task(self, number):
        try:
            if 0 <= number < len(self.journal):
                removed_task = self.journal.pop(number)
                self.save_to_file()
                print("Zadanie usunięte!")  
        except ValueError:
            print("Zadanie o takim numerze nie istnieje!")

def menu():
    print("\n Lista Zadań")
    print("1. Dodaj zadanie")
    print("2. Edytuj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zadania do pliku")
    print("5. Odczytaj zadania z pliku")
    print("6. Wyjdź")

def perform_actions(tasks_manager, action):
    if action == 1:
        task_content = input("Podaj treść zadania: ")
        tasks_manager.add_task(task_content)
    elif action == 2:
        try:
            task_number = int(input("Podaj numer zadania do edycji: "))
            new_task_content = input("Podaj nową treść zadania: ")
            tasks_manager.edit_task(task_number, new_task_content)
        except ValueError:
            print("Błędny numer zadania.")
    elif action == 3:
        try:
            task_number = int(input("Podaj numer zadania do usunięcia: "))
            tasks_manager.remove_task(task_number)
        except ValueError:
            print("Błędny numer zadania.")
    elif action == 4:
        tasks_manager.save_to_file()
        print("Zadania zapisane do pliku.")
    elif action == 5:
        tasks_manager.journal = tasks_manager.read_journal()
        print("Zadania odczytane z pliku.")

if __name__ == "__main__":
    tasks_manager = DziennikZajec()

    while True:
        menu()
        choice = input("Jaką operację chcesz wykonać? (1-6): ")

        if choice == '6':
            print("Do zobaczenia!")
            break

        try:
            action = int(choice)
            if 1 <= action <= 6:
                perform_actions(tasks_manager, action)
            else:
                print("Niepoprawny numer!")
        except ValueError:
            print("Niepoprawny numer!")