from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Synthetic training data
X = np.array([
    [50, 1000, 1, 1], [100, 50000, 0, 2], [80, 2000, 1, 0],
    [150, 100000, 0, 3], [60, 100, 1, 0]
])
y = ["fast", "slow", "moderate", "slow", "fast"]

model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, "model.pkl")
