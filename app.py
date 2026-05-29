import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SOLLWERT = 50.00
LSL = 49.80
USL = 50.20
ANZAHL_MESSWERTE = 100

np.random.seed(42)

messwerte = np.random.normal(
    loc=SOLLWERT,
    scale=0.06,
    size=ANZAHL_MESSWERTE
)

messwerte[70:] = messwerte[70:] + 0.08

df = pd.DataFrame({
    "Messung": np.arange(1, ANZAHL_MESSWERTE + 1),
    "Durchmesser_mm": messwerte
})

mittelwert = df["Durchmesser_mm"].mean()
standardabweichung = df["Durchmesser_mm"].std()
varianz = df["Durchmesser_mm"].var()

Cp = (USL - LSL) / (6 * standardabweichung)

Cpk = min(
    (USL - mittelwert) / (3 * standardabweichung),
    (mittelwert - LSL) / (3 * standardabweichung)
)

print("Qualitätsregelkarte mit Python")
print("------------------------------")
print(f"Mittelwert: {mittelwert:.4f} mm")
print(f"Varianz: {varianz:.6f}")
print(f"Standardabweichung: {standardabweichung:.4f} mm")
print(f"Cp: {Cp:.3f}")
print(f"Cpk: {Cpk:.3f}")

df.to_csv("messdaten_achsbolzen.csv", index=False)
print("CSV-Datei wurde gespeichert.")

warn_oben = mittelwert + 2 * standardabweichung
warn_unten = mittelwert - 2 * standardabweichung
eingriff_oben = mittelwert + 3 * standardabweichung
eingriff_unten = mittelwert - 3 * standardabweichung

plt.figure(figsize=(14, 7))
plt.plot(df["Messung"], df["Durchmesser_mm"], marker="o", label="Messwerte")

plt.axhline(mittelwert, linestyle="--", label="Mittelwert")
plt.axhline(warn_oben, linestyle=":", label="+2σ")
plt.axhline(warn_unten, linestyle=":", label="-2σ")
plt.axhline(eingriff_oben, linestyle="-.", label="+3σ")
plt.axhline(eingriff_unten, linestyle="-.", label="-3σ")
plt.axhline(USL, linestyle="-", label="USL")
plt.axhline(LSL, linestyle="-", label="LSL")

plt.title("Qualitätsregelkarte")
plt.xlabel("Messung")
plt.ylabel("Durchmesser [mm]")
plt.grid(True)
plt.legend()

plt.savefig("regelkarte.png")
plt.show()

print("Regelkarte wurde als regelkarte.png gespeichert.")