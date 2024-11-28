"""Cílem úkolu je vytvořit poznámkový blok V poznámkovém bloku můžeme přidávat,
 odebírat nebo měnit řádky. Když spustíme program tak máme následující možnosti:

Přidat poznámku (nakonec)
Vypsat všechny poznámky
Smazat poznámku (budeme vyzváni, jaký řádek smazat)
Upravit poznámku (budeve vyzváni, jaký řádek a jak upravit)
Uložit poznámky do souboru .csv (budeme vyzváni do jakého souboru)
(Volitelně uložení i přes pickle)
Načíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru)"""

import csv
import pickle

class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self):
        note = input(f"Zadejte svou poznamku zde: ")
        self.notes.append(note)
        print("Poznamka byla pridana.")

    def print_notes(self):
        if not self.notes:
            print(f"V ukolovniku nejsou zadne poznamky")
        else:
            print(f"Poznamky: ")
            for i, note in enumerate(self.notes):
                print(f"{i + 1}. {note}")

    def delete_note(self):
        try:
            if not self.notes:
                print("Nejsou zde zadne poznamky.")
                return

            num_delete = int(input(f"Zadejte cislo radku s poznamkou, kterou si prejete smazat: "))
            if 1 <= num_delete <= len(self.notes):
                deleted_note = self.notes.pop(num_delete - 1)
                print(f"Poznamka cislo {num_delete} byla smazana.")
            else:
                print(f"Pod zadanym cislem neexistuje poznamka.")
        except ValueError:
            print("Je treba zadat platne cislo.")


    def edit_note(self):
        try:
            if not self.notes:
                print(f"K dispozici neni zadna poznamka pro upravu.")
                return

            num_edit = int(input(f"Zadejte cislo poznamky, kterou chcete upravit: "))
            if 1 <= num_edit <= len(self.notes):
                new_note = input(f"Zadejte novou poznamku misto puvodni poznamky: ")
                self.notes[num_edit - 1] = new_note
                print(f"Poznamka cislo {num_edit} byla zmenena.")
            else:
                print(f"Pod timto cislem nebyla nalezena zadna poznamka.")
        except ValueError:
            print("Je treba zadat platne cislo.")

    def save_csv(self):
        filename = input("Zadejte nazev souboru pro ulozeni (s priponou .csv): ")
        if not ".csv" in filename:
            print("Soubor musi mit priponu .csv")
            return
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note])
        print(f"Poznamky byly ulozeny do souboru '{filename}'.")


    def load_csv(self):
        filename = input("Zadejte nazev souboru pro nacteni (s priponou .csv): ")

        if not ".csv" in filename:
            print("Soubor musi mit priponu .csv")
            return

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.notes = [row[0] for row in reader]
        print(f"Poznamky byly nacteny ze souboru '{filename}'.")

    def save_pickle(self):
        filename = input(f"Zadejte jmeno souboru pro ulozeni (s priponou .pkl): ")
        if not ".pkl" in filename:
            print("Soubor musi mit priponu .pkl")
            return
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)
        print(f"Poznamky byly ulozeny do souboru '{filename}' (pickle).")

    def load_pickle(self):
        filename = input("Zadejte nazev souboru pro nacteni (s priponou .csv): ")

        if not ".pkl" in filename:
            print("Soubor musi mit priponu .pkl")
            return

        with open(filename, 'rb') as file:
            self.notes = pickle.load(file)
        print(f"Poznamky byly nacteny ze souboru '{filename}'.")

def choose_action():
    notebook = Notes()
    while True:
        action = input(
            f"Vyberte, jaky ukon si prejete s poznamkami provest:"
            f" pridat, zobrazit, smazat, upravit, ulozit, nacist, "
            f"ulozit_pkl, nacist_pkl, ukoncit: ").lower()
        if action == "pridat":
            notebook.add_note()
        elif action == "zobrazit":
                notebook.print_notes()
        elif action == "smazat":
                notebook.delete_note()
        elif action == "upravit":
                notebook.edit_note()
        elif action == "ulozit":
                notebook.save_csv()
        elif action == "nacist":
                notebook.load_csv()
        elif action == "ulozit_pkl":
            notebook.save_pickle()
        elif action == "nacist_pkl":
                notebook.load_pickle()
        elif action == "ukoncit":
                print(f"Neplecha ukoncena.")
                break
        else:
            print(f"Zadali jste nepovoleny ukon. Zkuste to jeste jednou.")

choose_action()

# json tba