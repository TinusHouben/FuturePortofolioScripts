import pandas as pd
import numpy as np

n = 100000

data = {
    "product": np.random.choice(["Laptop", "Muis", "Toetsenbord", "Monitor", "Printer"], n),
    "regio": np.random.choice(["Noord", "Zuid", "Oost", "West"], n),
    "aantal": np.random.randint(1, 50, n),
    "prijs_per_stuk": np.random.uniform(10, 2000, n).round(2),
}

df = pd.DataFrame(data)
df["omzet"] = (df["aantal"] * df["prijs_per_stuk"]).round(2)

output_path = ""
df.to_csv(output_path, index=False, sep=';')
print(f"CSV opgeslagen op {output_path}")

print("\nEerste 5 rijen:")
print(df.head())

print("\nKolommen en types:")
print(df.info())

print("\nStatistieken:")
print(df.describe())

avg_omzet = df.groupby("product")["omzet"].mean()
print("\nGemiddelde omzet per product:")
print(avg_omzet)

total_omzet = df.groupby("regio")["omzet"].sum()
print("\nTotale omzet per regio:")
print(total_omzet)
