preparat = {
    "name":"noshpa",
    "amount":4,
    "category":"viccine",
    "save_temperature":25.0
    }


def check(preparat):
    result = {"name":preparat["name"],"temperature":"","category":""}
    if type(preparat["amount"]) !=int or type(preparat["save_temperature"]) != float:
        return "Помилка даних"
    
    if preparat["save_temperature"] < 5 : result["temperature"]= "Надто холодно"
    elif preparat["save_temperature"] > 25 : result["temperature"]= "Надто жарко"
    else : result["temperature"]= "Норма"
    
    match(preparat["category"]):
        case "antibiotic": result["category"]= "Рецептурний препарат"
        case "vitamin": result["category"]= "Вільний продаж"
        case "viccine": result["category"]= "Потребує спецзберігання"
        case _:result["category"]= "Невідома категорія"

    return result

print(check(preparat))