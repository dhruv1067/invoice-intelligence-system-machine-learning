import joblib 
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained classifier model
    """
    with open(model_path,"rb") as f:
        model = joblib.load(f)
    return model

def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices

    Parameters
    -----------
    input_data : dict

    Returns
    --------
    pd.DataFrame with predicted flag
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df)
    return input_df

if __name__ == "__main__":
    sample_data = {
        "invoice_quantity": [12, 5, 8, 20],
        "invoice_dollars": [18500, 9000, 3000, 2000],
        "Freight": [450, 120, 60, 40],
        "total_item_quantity": [15, 7, 10, 25],
        "total_item_dollars": [19000, 9300, 3150, 2100]
    }

    prediction = predict_invoice_flag(sample_data)
    print(prediction)