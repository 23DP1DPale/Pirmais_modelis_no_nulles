import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Nolasa attīrītos datus.
df = pd.read_csv("tirs.csv")

# Atdala pazīmes no prognozējamās kategorijas.
X = df.drop(columns=["Category"])
y = df["Category"]

# Pārveido dzimuma kategorijas skaitliskās vērtībās.
X = pd.get_dummies(X, columns=["Sex"], dtype=int)

# Sadala datus treniņa (80%) un testa (20%) daļās.
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Izveido un apmāca lēmumu koku.
modelis = DecisionTreeClassifier(max_depth=5, random_state=42)
modelis.fit(Xtr, ytr)

# Prognozē kategorijas treniņa un testa datos.
prognozes_tr = modelis.predict(Xtr)
prognozes_te = modelis.predict(Xte)

# Aprēķina modeļa precizitāti.
precizitate_tr = accuracy_score(ytr, prognozes_tr)
precizitate_te = accuracy_score(yte, prognozes_te)

# Nosaka biežāko kategoriju treniņa datos un aprēķina bāzes līniju.
biezaka_kategorija = ytr.mode()[0]
baze = (yte == biezaka_kategorija).mean()

print(f"Treniņa rindu skaits: {len(Xtr)}")
print(f"Testa rindu skaits: {len(Xte)}")
print(f"Biežākā kategorija: {biezaka_kategorija}")

print(f"\nTreniņa precizitāte: {precizitate_tr:.2%}")
print(f"Testa precizitāte: {precizitate_te:.2%}")
print(f"Bāzes līnija: {baze:.2%}")
print(f"Starpība: {(precizitate_te - baze) * 100:.2f} procentpunkti")

if precizitate_te > baze:
    print("Modelis pārspēj bāzes līniju.")
else:
    print("Modelis nepārspēj bāzes līniju.")

# Nosaka divas modelim svarīgākās kolonnas.
svarigums = pd.Series(modelis.feature_importances_, index=X.columns)
svarigums = svarigums.sort_values(ascending=False)

print("\nDivas svarīgākās kolonnas:")
print(svarigums.head(2))

# Atrod pirmo testa datu rindu, kurā modelis kļūdījās.
for i in range(len(yte)):
    if yte.iloc[i] != prognozes_te[i]:
        rindas_indekss = yte.index[i]

        print("\nNepareizas prognozes piemērs:")
        print(f"Rindas indekss: {rindas_indekss}")
        print(df.loc[rindas_indekss])
        print(f"Patiesā kategorija: {yte.iloc[i]}")
        print(f"Prognozētā kategorija: {prognozes_te[i]}")
        break
else:
    print("\nModelis testa datos nekļūdījās.")