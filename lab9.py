import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analyze_supplies(csv_path):
    data = pd.read_csv(csv_path)

    avg_price = np.mean(data["price_per_unit"])
    median_quantity = np.median(data["quantity"])
    std_price = np.std(data["price_per_unit"])

    data["total_price"] = data["quantity"] * data["price_per_unit"]

    supplier_profit = (
        data.groupby("supplier")["total_price"].sum().sort_values(ascending=False)
    )
    top_supplier = supplier_profit.index[0]
    top_supplier_profit = supplier_profit.iloc[0]

    total_by_category = data.groupby("category")["quantity"].sum()

    low_supply = data[data["quantity"] < 100]
    low_supply.to_csv("low_supply.csv", index=False)

    top3 = data.sort_values("total_price", ascending=False).head(3)
    print("🔝 Топ-3 постачання за total_price:")
    print(top3)

    plt.figure(figsize=(8, 5))
    total_by_category.plot(kind="bar")
    plt.title("Розподіл кількості препаратів за категоріями")
    plt.xlabel("Категорія")
    plt.ylabel("Сумарна кількість")
    plt.tight_layout()
    plt.savefig("category_distribution.png")
    plt.close()

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("ЗВІТ ПРО АНАЛІТИКУ ПОСТАЧАНЬ\n")
        f.write("===============================\n\n")
        f.write(f"Середня ціна всіх препаратів: {avg_price:.2f}\n")
        f.write(f"Медіана кількості: {median_quantity}\n")
        f.write(f"Стандартне відхилення ціни: {std_price:.2f}\n\n")
        f.write(f"Постачальник з найбільшим прибутком: {top_supplier}\n")
        f.write(f"Його прибуток: {top_supplier_profit:.2f}\n\n")
        f.write("Файл із дефіцитними поставками: low_supply.csv\n")
        f.write("Графік: category_distribution.png\n")

    print("\n✅ Звіт збережено у report.txt")
    print("✅ Графік збережено у category_distribution.png")
    print("✅ Файл із дефіцитними поставками: low_supply.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Аналіз даних постачань")
    parser.add_argument(
        "csv_path", type=str, help="Шлях до CSV-файлу з даними (наприклад, supplies.csv)"
    )
    args = parser.parse_args()

    analyze_supplies(args.csv_path)
