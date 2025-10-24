# Вхідні дані (приклад)
clients = [
    {"ім'я": "Анна", "сума угоди": 85, "статус перевірки": "clean"},
    {"ім'я": "Богдан", "сума угоди": 450, "статус перевірки": "suspicious"},
    {"ім'я": "Сергій", "сума угоди": 1200, "статус перевірки": "fraud"},
    {"ім'я": "Ірина", "сума угоди": "помилка", "статус перевірки": "clean"},
    {"ім'я": "Марія", "сума угоди": 700, "статус перевірки": "unknown"},
]

results = []

for client in clients:
    name = client.get("ім'я", "Невідомо")
    amount = client.get("сума угоди")
    status = client.get("статус перевірки", "").lower()

    # Перевірка типу даних
    if not isinstance(amount, (int, float)):
        results.append({
            "name": name,
            "category": "Фальшиві дані",
            "decision": "Не розглядати"
        })
        continue

    # Класифікація по сумі
    if amount < 100:
        category = "Дрібнота"
    elif amount < 1000:
        category = "Середнячок"
    else:
        category = "Великий клієнт"

    # Вибір рішення за статусом
    match status:
        case "clean":
            decision = "Працювати без питань"
        case "suspicious":
            decision = "Перевірити документи"
        case "fraud":
            decision = "У чорний список"
        case _:
            decision = "Невідомий статус"

    results.append({
        "name": name,
        "category": category,
        "decision": decision
    })

# Вивід результатів
for r in results:
    print(f"{r['name']}: {r['category']} — {r['decision']}")
