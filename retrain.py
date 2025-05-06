# app/retrain.py

import os
from model import train_model, save_model

def main(csv_path=None):
    print("Retraining model...")

    # Automatically resolve full path relative to this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_path = r'D:\FIVERR\text_intent_system\data\SEOLeadDataset.csv'

    csv_path = csv_path or default_path

    if not os.path.exists(csv_path):
        print(f"Error while training model: Dataset not found at {csv_path}")
        return

    try:
        model = train_model(csv_path)
        save_model(model)
        print(f"Model retrained and saved successfully from: {csv_path}")
    except Exception as e:
        print(f"Error while training model: {e}")

if __name__ == "__main__":
    main()
