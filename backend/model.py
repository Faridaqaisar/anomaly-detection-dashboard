import random
import numpy as np
from sklearn.ensemble import IsolationForest

BASELINE = 50
STD_DEV = 5
SPIKE_CHANCE = 0.08


def generate_reading():
    value = random.gauss(BASELINE, STD_DEV)
    is_injected_anomaly = False
    if random.random() < SPIKE_CHANCE:
        value += random.choice([-1, 1]) * random.uniform(25, 50)
        is_injected_anomaly = True
    return round(value, 2), is_injected_anomaly


def train_model():
    normal_data = np.array([random.gauss(BASELINE, STD_DEV) for _ in range(500)]).reshape(-1, 1)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(normal_data)
    return model


model = train_model()


def anomaly_score(value):
    return model.decision_function(np.array([[value]]))[0]


def is_anomaly(value, threshold=0.0):
    score = anomaly_score(value)
    return score < threshold


if __name__ == "__main__":
    for i in range(20):
        val, injected = generate_reading()
        score = anomaly_score(val)
        flagged = is_anomaly(val, threshold=0.0)
        marker = "ANOMALY" if flagged else "normal"
        print(f"value={val:>8}  score={score:.4f}  {marker}  (injected spike: {injected})")