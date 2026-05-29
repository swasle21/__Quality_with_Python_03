# Qualitätsregelkarten, Six Sigma und Prozessfähigkeit mit Python

## Aufgabenstellung

Für einen simulierten Achsbolzenprozess wurden Messdaten erzeugt und statistisch ausgewertet.

### Vorgaben

- Sollwert: 50,00 mm
- LSL (Lower Specification Limit): 49,80 mm
- USL (Upper Specification Limit): 50,20 mm
- 100 Messwerte
- Standardabweichung: 0,06 mm
- Prozessdrift von +0,08 mm ab Messwert 70

---

## Durchgeführte Schritte

1. Messdaten mit Python simuliert
2. Prozessdrift eingebaut
3. Messwerte visualisiert
4. Statistische Kennwerte berechnet
   - Mittelwert
   - Varianz
   - Standardabweichung
   - Minimum
   - Maximum
5. Qualitätsregelkarte erstellt
6. Cp und Cpk berechnet
7. Normalverteilung mit Shapiro-Wilk-Test geprüft
8. CSV-Datei exportiert

---

## Ergebnisse

Die Qualitätsregelkarte zeigt eine erkennbare Prozessdrift ab Messung 70.

Der berechnete Cpk-Wert liegt unter dem Cp-Wert, was darauf hinweist, dass der Prozess gegenüber dem Sollwert verschoben ist.

---

## Dateien

- `notebook.ipynb` – vollständige Ausarbeitung
- `app.py` – Python-Anwendung
- `messdaten_achsbolzen.csv` – exportierte Messdaten
- `regelkarte.png` – Screenshot der Qualitätsregelkarte

---

## Verwendete Bibliotheken

- NumPy
- Pandas
- Matplotlib
- SciPy

---

## Autor

Simon Wasle
