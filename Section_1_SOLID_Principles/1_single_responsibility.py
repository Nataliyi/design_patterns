""" 1е правило основных принципов - SRP
Правило одиночной отвественности
У каждого класса должна быть только одна ответственность и
все поведения класса должны быть направлены только на обеспечение
этой ответственности"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

# данный метод нарушает правило, так как добавляет ответственности
# к классу, уже имеющему одну ответственность - записывать мысли

    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

# создадим класс с еще одной ответственностью - сохранять журналы в файлы


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
