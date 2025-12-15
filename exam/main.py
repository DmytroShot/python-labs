import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def load_data(path):
    try:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        elif path.endswith(".json"):
            return pd.read_json(path)
        elif path.endswith(".tsv"):
            return pd.read_csv(path, sep="\t")
        else:
            raise ValueError("Непідтримуваний формат")
    except Exception as e:
        print(f"Помилка при завантаженні {path}: {e}")
        return None


file1 = "data1.csv"
file2 = "data2.csv"

with ThreadPoolExecutor(max_workers=2) as executor:
    df1, df2 = executor.map(load_data, [file1, file2])


if df1 is None and df2 is None:
    raise RuntimeError("Обидва файли недоступні")

elif df1 is None:
    final_df = df2

elif df2 is None:
    final_df = df1

else:
    final_df = pd.merge(df1, df2, on="id", how="outer")

    if "name_x" in final_df.columns and "name_y" in final_df.columns:
        final_df["name"] = final_df["name_x"].combine_first(final_df["name_y"])
        final_df = final_df.drop(columns=["name_x", "name_y"])

print(final_df.head())

final_df.to_csv("final_result.csv", index=False)
