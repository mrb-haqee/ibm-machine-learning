import json
import pandas as pd
from ml import mlibm
from flask import Flask, request as req, jsonify
from flask_cors import CORS

# machine learning IBM
file_path = "ml/data/dataset_bmi.csv"
predictor = mlibm.BMIPredictor(file_path)
# predictor.summary_dataset() # Summary dataset
predictor.train_model()  # Train the model

# SERVER
app = Flask(__name__)
CORS(app)
@app.route("/predict", methods=["POST"])
def cek():
    gender = req.form.get('gender')
    height = int(req.form.get('height'))
    weight = int(req.form.get('weight'))

    # Buat DataFrame dari data yang diterima
    input_data = pd.DataFrame({
        "Gender": [gender],
        "Height": [height],
        "Weight": [weight]
    })

    predictions = predictor.predict_sample(input_data)
    return predictions[0]

if __name__ == "__main__":
    app.run()
