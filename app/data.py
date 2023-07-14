import pandas as pd
from app.config import FILES_INPUT_DIR
import os


def calculate_data_average():
    file_path = os.path.join(FILES_INPUT_DIR, 'people_data.csv')

    data = pd.read_csv(file_path)

    average_height_cm = data["Height"].mean()
    average_weight_kg = data["Weight"].mean()

    print(f"Average height: {average_height_cm} cm")
    print(f"Average weight: {average_weight_kg} kg")
