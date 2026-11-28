
# Rezultātu interpretācija

## 1. Kas ir šie dati un no kurienes tie nāk?

Darbā izmantoju HCV Data datu kopu, kas lejupielādēta no UCI Machine Learning Repository. Datu kopa satur informāciju par asins donoriem un pacientiem ar aknu slimībām, tostarp viņu vecumu, dzimumu un asins analīžu rezultātiem.

Sākotnējā datu kopā bija 615 rindas un 14 kolonnas. Prognozējamā kolonna ir `Category`, kas norāda pacienta kategoriju.

Datu avots: https://archive.ics.uci.edu/dataset/571/hcv+data

## 2. Kas ar datiem bija nepareizi un ko tu ar tiem izdarīji?

Datu kopā bija nevajadzīga ierakstu kārtas numuru kolonna `Unnamed: 0` un rindas ar trūkstošām vērtībām.

Izņēmu kārtas numuru kolonnu, jo tā nesatur modelim noderīgu medicīnisko informāciju. Pārbaudīju arī dublikātus, taču neviens netika atrasts.

Rindas ar trūkstošām vērtībām izmetu, izmantojot `dropna()`, jo nevēlējos aizstāt nezināmus medicīniskos rādītājus ar aprēķinātām vērtībām.

- Sākotnējais rindu skaits: 615.
- Izmestās dublikātu rindas: 0.
- Izmestās rindas ar trūkstošām vērtībām: 26.
- Kopā izmestās rindas: 26 (4,23%).
- Rindu skaits pēc tīrīšanas: 589.

Attīrītos datus saglabāju failā `tirs.csv`, nemainot oriģinālo failu.

## 3. Ko modelis prognozē un cik labi?

Modelis prognozē pacienta kategoriju pēc vecuma, dzimuma un asins analīžu rezultātiem.

Izmantoju lēmumu koka klasifikatoru (`DecisionTreeClassifier`) ar maksimālo dziļumu 5. Datus sadalīju treniņa daļā (80%) un testa daļā (20%).

| Rādītājs | Rezultāts |
|---|---:|
| Treniņa rindu skaits | 471 |
| Testa rindu skaits | 118 |
| Treniņa precizitāte | 98,30% |
| Testa precizitāte | 93,22% |
| Bāzes līnija | 88,98% |
| Starpība | 4,24 procentpunkti |

Bāzes līnija tika aprēķināta, vienmēr prognozējot treniņa datos biežāk sastopamo kategoriju `0=Blood Donor`.

Modelis pareizi prognozēja 110 no 118 testa ierakstiem, savukārt bāzes līnija nodrošināja 105 pareizas prognozes.

Modelis pārspēj bāzes līniju par 4,24 procentpunktiem. Starpība nav īpaši liela, jo modelis pareizi prognozēja tikai par pieciem ierakstiem vairāk.

Treniņa precizitāte ir par 5,08 procentpunktiem augstāka nekā testa precizitāte. Tas varētu nozīmēt, ka modelis ir nedaudz pārmācījies.

## 4. Kuras divas kolonnas izrādījās svarīgākās un vai tas ir loģiski?

| Kolonna | Svarīgums |
|---|---:|
| AST (aspartātaminotransferāze) | 48,46% |
| ALB (albumīns) | 18,90% |

Šāds rezultāts ir loģisks, jo abi asins analīžu rādītāji ir saistīti ar aknu veselību.

Paaugstināts AST līmenis var liecināt par aknu šūnu bojājumiem, savukārt pazemināts albumīna līmenis var būt saistīts ar aknu darbības traucējumiem.

Tomēr šie rezultāti parāda pazīmju svarīgumu konkrētajā modelī, nevis to nozīmi medicīniskajā diagnostikā kopumā.

## 5. Vienas nepareizas prognozes piemērs

Modelis kļūdījās ierakstā ar indeksu 34 failā `tirs.csv`.

| Kolonna | Vērtība |
|---|---|
| Category | 0=Blood Donor |
| Age | 35 |
| Sex | m |
| ALB | 42.1 |
| ALP | 68.3 |
| ALT | 37.2 |
| AST | 56.2 |
| BIL | 11.1 |
| CHE | 9.3 |
| CHOL | 4.63 |
| CREA | 99.0 |
| GGT | 16.8 |
| PROT | 73.6 |

- Patiesā kategorija: `0=Blood Donor`.
- Prognozētā kategorija: `1=Hepatitis`.

Manuprāt, modelis varēja kļūdīties AST rādītāja dēļ, jo tas ir svarīgākais rādītājs apmācītajā modelī un šī ieraksta AST vērtība ir 56,2. Iespējams, ka šī vērtība kopā ar citiem rādītājiem bija līdzīga hepatīta kategorijas pacientu datiem.

Precīzs kļūdas iemesls netika pārbaudīts.

## 6. Ko ar šo modeli nedrīkst darīt?

Šo modeli nedrīkst izmantot aknu slimību diagnosticēšanai reāliem pacientiem.

Modelis ir apmācīts ar nelielu un nelīdzsvarotu datu kopu, kurā lielākā daļa ierakstu pieder asins donoru kategorijai. Modelis var kļūdīties, un tas nav pārbaudīts izmantošanai medicīnas praksē.

Ja modelis kļūdītos, pacientam varētu noteikt nepareizu diagnozi vai nepamanīt slimību.

## Pašvērtējums

Man izdevās attīrīt datus, apmācīt lēmumu koka modeli un iegūt rezultātu, kas pārspēj bāzes līniju.

Man neizdevās pareizi prognozēt visus testa ierakstus, un modeļa uzlabojums salīdzinājumā ar bāzes līniju nebija ļoti liels.

Nākamreiz es izmēģinātu dažādus lēmumu koka dziļumus un pārbaudītu, cik labi modelis prognozē katru pacientu kategoriju atsevišķi.
