import csv
import random

# Generate 50 records with actual and predicted values
records = []
for i in range(50):
    actual = random.uniform(10, 100)
    predicted = actual + random.uniform(-5, 5)  # add small noise
    records.append({'actual': round(actual, 2),
                   'predicted': round(predicted, 2)})

# Save to CSV
csv_path = "predictions.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["actual", "predicted"])
    writer.writeheader()
    writer.writerows(records)

csv_path


# Create