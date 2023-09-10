import csv
import random


class BMIGenerator:
    def __init__(self):
        self.gender = random.choice(["Male", "Female"])
        self.height = self.generate_random_height()
        self.weight = self.generate_random_weight()
        self.bmi = self.calculate_bmi()
        self.status = self.determine_status()

    def generate_random_height(self):
        if self.gender == "Female":
            return random.uniform(1.47, 1.83)
        else:
            return random.uniform(1.57, 1.93)

    def generate_random_weight(self):
        if self.gender == "Female":
            return random.uniform(42, 100)
        else:
            return random.uniform(51, 120)

    def calculate_bmi(self):
        return self.weight / (self.height**2)

    def determine_status(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi <= 22.9:
            return "Normal"
        elif 22.9 < self.bmi <= 24.9:
            return "Overweight"
        elif 24.9 < self.bmi <= 29.9:
            return "Obesity I"
        else:
            return "Obesity II"

    def get_bmi_data(self):
        return {
            "Gender": self.gender,
            "Height": round(self.height * 100),
            "Weight": round(self.weight),
            "BMI": self.bmi,
            "Status": self.status,
        }


# Buat dataset dengan 1000 nilai BMI acak berdasarkan jenis kelamin dan status
bmi_generator = BMIGenerator()
dataset = []
for _ in range(1000):
    bmi_data = bmi_generator.get_bmi_data()
    dataset.append(bmi_data)

# Simpan dataset ke dalam file CSV
with open("data/dataset_bmi.csv", "w", newline="") as csvfile:
    fieldnames = ["Gender", "Height", "Weight", "BMI", "Status"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for bmi_data in dataset:
        writer.writerow(bmi_data)

print("Dataset BMI telah dibuat dan disimpan dalam file 'dataset_bmi.csv'.")
