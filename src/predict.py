import joblib
import pandas as pd
from preprocessing import clean_data

model = joblib.load("artifacts/model.pkl")
feature_columns = joblib.load("artifacts/feature_columns.pkl")
input_df = pd.read_csv("data/ai4i2020.csv")

input_df = clean_data(input_df)

input_df = input_df.reindex(
    columns=feature_columns,
    fill_value=0
)

prediction = model.predict(input_df)