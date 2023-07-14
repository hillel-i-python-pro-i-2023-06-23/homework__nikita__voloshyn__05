from faker import Faker
import requests
import pandas as pd

# 1
def get_file_content():
        with open('test_text.txt', 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            return content



# 2
def generate_user_data(num_users=100):
    fake = Faker()
    users = []

    for _ in range(num_users):
        name = fake.first_name()
        email = fake.email()
        user_data = f"{name} {email}"
        users.append(user_data)

    return users

user_data = generate_user_data()

for user in user_data:
    print(user)


# 3

    def get_number_of_astronauts():
        url = "http://api.open-notify.org/astros.json"

        response = requests.get(url)
        data = response.json()

        number_of_astronauts = data["number"]
        astronauts = data["people"]

        return number_of_astronauts, astronauts

    count, astronaut_list = get_number_of_astronauts()

    print(
        f"dangles around orbit: {count} ")

    print("names:")
    for astronaut in astronaut_list:
        print(astronaut["name"])


# 4
def data_averag():
    data = pd.read_csv('people_data.csv')

    average_height_cm = data["Height"].mean()
    average_weight_kg = data["Weight"].mean()

    print(f"Average height: {average_height_cm} см")
    print(f"Average weight: {average_weight_kg} кг")

data_averag()
def main():
    get_file_content()
    generate_user_data()
    get_number_of_astronauts()
    data_averag()



