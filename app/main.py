from app.helpers import get_file_content, generate_user_data, print_user_data
from app.astronauts import print_astronaut_data
from app.data import calculate_data_average


def main():
    print("1")
    file_content = get_file_content()
    print(file_content)
    print("2")
    print_user_data(generate_user_data())
    print("3")
    print_astronaut_data()
    print("4")
    calculate_data_average()


if __name__ == "__main__":
    main()
