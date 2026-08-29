import pandas as pd

df = pd.read_csv("Sample_Superstore.csv")

print(df.shape)
print("liczba kolumn:", df.shape[1])
print(df.head())

statystyki_produktow = df.groupby("Product Name")["Sales"].sum()
top5 = statystyki_produktow.sort_values(ascending=False).head(5)
print("Top 5 produktów:")
print(top5)

srednia_wartosc = df["Sales"].mean()
print("Średnia wartość zamówienia:", srednia_wartosc)

df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Miesiac"] = df["Order Date"].dt.to_period("M").astype(str)

miesieczne_sumy = df.groupby("Miesiac")["Sales"].sum()
print("Miesięczne sumy sprzedaży:")
print(miesieczne_sumy)

