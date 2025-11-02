import pandas as pd
import time

csv_path = ""
df = pd.read_csv(csv_path, sep=';')

print("Dataset ingelezen. Aantal rijen:", len(df))
print(df.head())

start_time = time.time()

west_df = df[df['regio'] == 'West']

avg_omzet_per_product = west_df.groupby('product')['omzet'].mean()
total_omzet_per_product = west_df.groupby('product')['omzet'].sum()
total_omzet_per_regio = df.groupby('regio')['omzet'].sum()

end_time = time.time()
elapsed_time = end_time - start_time

print("\nAnalyse uitgevoerd in {:.4f} seconden".format(elapsed_time))
print("\nGemiddelde omzet per product in regio West:")
print(avg_omzet_per_product)
print("\nTotale omzet per product in regio West:")
print(total_omzet_per_product)
print("\nTotale omzet per regio:")
print(total_omzet_per_regio)

summary_path = ""
summary_df = df.groupby(['regio', 'product']).agg(
    totaal_omzet=('omzet', 'sum'),
    gemiddelde_omzet=('omzet', 'mean'),
    aantal_transacties=('omzet', 'count')
).reset_index()

summary_df.to_csv(summary_path, index=False, sep=';')
print(f"Samenvatting opgeslagen als: {summary_path}")
