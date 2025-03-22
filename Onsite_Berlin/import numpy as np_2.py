import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Anzahl der Zeilen und Spalten
data_rows = 10000
data_columns = 11

# Biologische Daten simulieren
columns = [
    "Protein Expression", "Gene Mutation Rate", "Cell Growth Rate", "Enzyme Activity", "Metabolite Level",
    "Hormone Concentration", "Blood Oxygen Level", "Neurotransmitter Activity", "DNA Methylation", "RNA Expression",
    "Body Temperature"
]

data = np.random.normal(loc=0, scale=1, size=(data_rows, data_columns))  # Generierung normalverteilter Daten

# Einführung von Anomalien
num_anomalies = int(0.01 * data_rows)  # 1% der Daten als Anomalien
anomaly_indices = np.random.choice(data_rows, num_anomalies, replace=False)

# Zufällige Anomalien in einigen Spalten
for i in anomaly_indices:
    col = np.random.choice(data_columns, size=np.random.randint(1, 4))  # 1 bis 3 Spalten pro Anomalie
    data[i, col] = data[i, col] * np.random.uniform(5, 15, size=len(col))  # Werte extrem erhöhen

# Daten als DataFrame speichern
df = pd.DataFrame(data, columns=columns)

print(df.head)