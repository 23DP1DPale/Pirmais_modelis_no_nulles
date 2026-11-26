import pandas as pd

# Nolasa oriģinālo CSV failu, lai apstrādātu neapstrādātos datus.
df = pd.read_csv("dati/hcvdat0.csv")

rindu_sk_sakum = len(df)
print(f"Rindu skaits sākumā: {rindu_sk_sakum}")

# Izņem ierakstu kārtas numuru kolonnu, jo tā nesatur medicīnisku informāciju.
df = df.drop(columns=["Unnamed: 0"])

# Noņem iespējamos dublētos pacientu ierakstus, lai tie neietekmētu modeļa apmācību.
pirms = len(df)
df = df.drop_duplicates()
dublikati = pirms - len(df)

# Izņem rindas ar trūkstošām vērtībām, jo dažiem pacientiem nav visu analīžu rezultātu.
pirms = len(df)
df = df.dropna()
trukstosas = pirms - len(df)

# Saglabā attīrītos datus jaunā CSV failā, nemainot oriģinālo failu.
df.to_csv("tirs.csv", index=False)

print(f"Izmestās dublikātu rindas: {dublikati}")
print(f"Izmestās rindas ar trūkstošām vērtībām: {trukstosas}")
print(f"Kopā izmestās rindas: {rindu_sk_sakum - len(df)}")
print(f"Rindu skaits beigās: {len(df)}")
print("Attīrītie dati saglabāti failā tirs.csv")