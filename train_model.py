import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("mental_health_data.csv")

# Split into features and label
X = df.drop('label', axis=1)
y = df['label']

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")

