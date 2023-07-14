from faker import Faker
from pathlib import Path

def get_file_content():
    file_path = Path(__file__).parent / "input_files" / "test_text.txt"
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def generate_user_data(num_users=100):
    fake = Faker()
    users = []

    for _ in range(num_users):
        name = fake.first_name()
        email = fake.email()
        user_data = f"{name} {email}"
        users.append(user_data)

    return users


def print_user_data(user_data):
    for user in user_data:
        print(user)
