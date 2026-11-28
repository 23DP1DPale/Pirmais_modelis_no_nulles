
# Pirmais modelis no nulles

## Projekta apraksts

Šajā projektā izmantoju HCV Data datu kopu, lai apmācītu mašīnmācīšanās modeli, kas prognozē pacienta kategoriju pēc vecuma, dzimuma un asins analīžu rezultātiem.

Projektā tiek veikta datu tīrīšana, lēmumu koka modeļa apmācīšana, testēšana un rezultātu salīdzināšana ar bāzes līniju.

## Datu avots

HCV Data - UCI Machine Learning Repository.

https://archive.ics.uci.edu/dataset/571/hcv+data

## Nepieciešamās bibliotēkas

- pandas
- scikit-learn

Bibliotēku uzstādīšana:

```bash
pip install pandas scikit-learn
```

## Projekta palaišana

1. Palaist datu tīrīšanas skriptu:

```bash
python 01_tirisana.py
```

Skripts attīra sākotnējos datus un saglabā tos failā `tirs.csv`.

2. Palaist modeļa apmācīšanas un testēšanas skriptu:

```bash
python 02_modelis.py
```

Skripts apmāca modeli un izvada tā precizitāti, bāzes līniju, divas svarīgākās pazīmes un nepareizas prognozes piemēru.

## Rezultāti

Modeļa testa precizitāte ir 93,22%, bet bāzes līnija ir 88,98%.

Detalizēta rezultātu analīze un pašvērtējums ir pieejami failā [rezultati.md](rezultati.md).

Modelis ir izveidots mācību nolūkiem un nav paredzēts medicīniskajai diagnostikai.
