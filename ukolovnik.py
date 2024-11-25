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

class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self):
        note = input(f"Zadejte svou poznamku zde: ")
        self.notes.append(note)

    def print_notes(self):
        if not notes in self.notes:
            print(f"V ukolovniku nejsou zadne poznamky")
        else:
            print(self.notes)

    def delete_note(self):
        self.print_notes()
        cislo_smazat = input(f"Zadejte cislo radku s poznamkou, kterou si prejete smazat: ")

    def edit_note(self):
        pass

# ulozit do csv = vyzva do jakeho, import asi nahore a ulozit pres writer
    def save_csv(self):
        pass

# nacist z csv = vyzva z ktereho souboru a nacist pres reader
    def load_csv(self):
        pass