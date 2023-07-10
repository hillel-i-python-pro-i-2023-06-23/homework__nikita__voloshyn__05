from faker import Faker

def generate_random_content()->str:
    fake = Faker()
    content = fake.sentence()
    print(content)
    return content

def main():
    generate_random_content()