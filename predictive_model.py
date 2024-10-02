import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import google.generativeai as genai

genai.configure(api_key='AIzaSyDUUsTEvKKRya7u46jEJw4OMwFZ3dRKIRs')

def generate_additional_features(sales_data):
    def create_prompt(row):
        return f"Given that the economic conditions are {row['economic_conditions']}, and sales data for {row['sales']} units of {row['product_name']}, what is the expected impact on inventory demand?"

    sales_data['gen_feature'] = sales_data.apply(lambda row: float(
        genai.generate_text(prompt=create_prompt(row), max_output_tokens=5).candidates[0].output.strip()), axis=1)
    
    return sales_data

def train_predictive_model(sales_data):
    # Remove columns that aren't features for training
    features = sales_data.drop(['sales', 'date', 'product_name', 'economic_conditions'], axis=1)
    target = sales_data['sales']

    # Train a Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, target)
    return model

def predict_sales(model, future_data):
    predictions = model.predict(future_data)
    return predictions