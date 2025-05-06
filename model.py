# app/model.py

import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from utils import clean_text
import pandas as pd

MODEL_PATH = "trained_model/model.pkl"

def load_model():
    """
    Loads the trained model from the file.
    Raises FileNotFoundError if the model file is not found.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not found. Please run retrain.py first.")
    return joblib.load(MODEL_PATH)

def save_model(model):
    """
    Saves the trained model to the file.
    """
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)

def train_model(csv_path="data/SEOLeadDataset.csv"):
    """
    Trains a new model using the provided CSV file and saves the trained model.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at {csv_path}")
    
    df = pd.read_csv(csv_path)
    df.dropna(subset=["text", "label"], inplace=True)
    df["text"] = df["text"].apply(clean_text)

    X = df["text"]
    y = df["label"]

    # Define a pipeline with TfidfVectorizer and Logistic Regression
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=200))
    ])

    # Fit the model to the data
    pipeline.fit(X, y)
    return pipeline

def predict(model, text):
    """
    Makes a prediction using the loaded model for the provided text.
    """
    cleaned = clean_text(text)
    return model.predict([cleaned])[0]
