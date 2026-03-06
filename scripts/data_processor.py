import pandas as pd
import random
from datetime import datetime, timedelta

def generate_data(records=100):
    dates = [datetime.now() - timedelta(days=x) for x in range(records)]
    data = {
        'Date': dates,
        'Feature': [random.choice(['Share Basket', 'Onboarding']) for _ in range(records)],
        'Friction_Detected': [random.choice([0, 1]) for _ in range(records)],
        'Sentiment': [random.uniform(0, 1) for _ in range(records)]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_data()
    df.to_csv("product_metrics.csv", index=False)
    print("✅ Data ready for Power BI.")
