import requests


def get_number_of_astronauts():
    url = "http://api.open-notify.org/astros.json"

    response = requests.get(url)
    data = response.json()

    number_of_astronauts = data["number"]
    astronauts = data["people"]

    return number_of_astronauts, astronauts


def print_astronaut_data():
    count, astronaut_list = get_number_of_astronauts()
    print(f"Number of astronauts in orbit: {count}")
    print("Astronaut names:")
    for astronaut in astronaut_list:
        print(astronaut["name"])
