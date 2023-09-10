from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

class BMIDataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def read_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")

    def get_summary_statistics(self):
        if self.df is not None:
            return self.df.describe()
        else:
            print("Data not loaded. Please call read_data() first.")

    def get_gender_count(self):
        if self.df is not None:
            return self.df['Gender'].value_counts()
        else:
            print("Data not loaded. Please call read_data() first.")

    def get_status_count(self):
        if self.df is not None:
            return self.df['Status'].value_counts()
        else:
            print("Data not loaded. Please call read_data() first.")

    def get_mean_bmi_by_gender(self):
        if self.df is not None:
            return self.df.groupby('Gender')['BMI'].mean()
        else:
            print("Data not loaded. Please call read_data() first.")

class BMIPredictor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model = DecisionTreeClassifier()
        self.label_encoder = LabelEncoder()
        self.data = pd.read_csv(self.file_path)
        
    def summary_dataset(self):
        bmi_data_analyzer = BMIDataAnalyzer(self.file_path)
        bmi_data_analyzer.read_data()

        print("Ringkasan Statistik Data BMI:")
        print(bmi_data_analyzer.get_summary_statistics())

        print("\nJumlah Pria dan Wanita:")
        print(bmi_data_analyzer.get_gender_count())

        print("\nJumlah Status BMI:")
        print(bmi_data_analyzer.get_status_count())

        print("\nRata-rata BMI berdasarkan Jenis Kelamin:")
        print(bmi_data_analyzer.get_mean_bmi_by_gender())


    def preprocess_data(self):
        X = self.data[["Gender", "Height", "Weight", "BMI"]]
        y = self.data["Status"]
        X["Gender"] = self.label_encoder.fit_transform(X["Gender"])
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Akurasi Model: {accuracy * 100:.2f}%")

    def predict_sample(self, sample_data):
        sample_data["Gender"] = self.label_encoder.transform(sample_data["Gender"])
        sample_data["BMI"] = (
            sample_data["Weight"] / (sample_data["Height"] / 100) ** 2
        )
        input_prediction = self.model.predict(sample_data)
        status_mapping = {
            label: status for label, status in zip(self.model.classes_, self.data["Status"].unique())
        }
        input_prediction = [status_mapping[prediction] for prediction in input_prediction]
        return input_prediction
