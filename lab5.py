class JunkItem:
    def __init__(self, name, quantity, value):
        self.name = name
        self.quantity = quantity
        self.value = value

    def __str__(self):
        return f"{self.name}, {self.quantity}, {self.value}"


class JunkStorage:
    @staticmethod
    def serialize(items, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for item in items:
                file.write(f"{item.name} | {item.quantity} | {item.value}\n")
    
    @staticmethod
    def parse(filename):
        items = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.strip().split(" | ")
                
                if len(fields) != 3:
                    print(f"Попередження: рядок не містить трьох полів: {line.strip()}")
                    continue
                
                try:
                    quantity = int(fields[1])
                except ValueError:
                    print(f"Попередження: кількість не є числом: {fields[1]}")
                    continue
                
                try:
                    value = float(fields[2].replace(',', '.'))
                except ValueError:
                    print(f"Попередження: ціна не є числом з плаваючою точкою: {fields[2]}")
                    continue
                
                items.append(JunkItem(fields[0], quantity, value))
        
        return items


items = [
    JunkItem("Бляшанка", 5, 2.5),
    JunkItem("Стара плата", 3, 7.8),
    JunkItem("Купка дротів", 10, 1.2)
]

filename = "junk_storage.csv"

JunkStorage.serialize(items, filename)
print(f"Товари записані у файл {filename}.")

parsed_items = JunkStorage.parse(filename)
print("\nЗчитані елементи:")
for item in parsed_items:
    print(item)
