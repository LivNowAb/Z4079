"""Cílem úkolu je vytvořit poznámkový blok V poznámkovém bloku můžeme přidávat,
 odebírat nebo měnit řádky. Když spustíme program tak máme následující možnosti:

Přidat poznámku (nakonec)
Vypsat všechny poznámky
Smazat poznámku (budeme vyzváni, jaký řádek smazat)
Upravit poznámku (budeve vyzváni, jaký řádek a jak upravit)
Uložit poznámky do souboru .csv (budeme vyzváni do jakého souboru)
(Volitelně uložení i přes pickle)
Načíst poznámky ze souboru .csv (budeme vyzváni z jakého souboru)"""

# import csv asi

class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self):
        note = input(f"Zadejte svou poznamku zde: ")
        self.notes.append(note)

    def print_notes(self, note):
        if note not in self.notes:
            print(f"V ukolovniku nejsou zadne poznamky")
        else:
            print(self.notes)

    def delete_note(self, num_delete):
        num_delete = int(input(f"Zadejte cislo radku s poznamkou, kterou si prejete smazat: "))
        if 0 <= num_delete <= len(self.notes):
            deleted_note = self.notes.remove(num_delete)
            print(f"Poznamka cislo {num_delete} byla smazana.")
        else:
            print(f"Pod zadanym cislem neexistuje poznamka.")

    def edit_note(self):
        num_edit = int(input(f"Zadejte cislo poznamky, kterou chcete smazat: "))
        if 0 <= num_edit <= len(self.notes):
            new_note = input(f"Zadejte novou poznamku misto prave smazane.")
            self.notes[num_edit] = new_note
            print(f"Poznamka cislo {num_edit} byla zmenena.")
        else:
            print(f"Pod timto cislem nebyla nalezena zadna poznamka.")

# ulozit do csv = vyzva do jakeho, import asi nahore a ulozit pres writer, tba
    def save_csv(self):
        pass

# nacist z csv = vyzva z ktereho souboru a nacist pres reader, tba
    def load_csv(self):
        pass

