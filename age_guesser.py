import requests

def main():
    epic_title = "     _    ____ _____    ____ _   _ _____ ____ ____  _____ ____\n    / \  / ___| ____|  / ___| | | | ____/ ___/ ___|| ____|  _ \ \n   / _ \| |  _|  _|   | |  _| | | |  _| \___ \___ \|  _| | |_) |\n  / ___ \ |_| | |___  | |_| | |_| | |___ ___) |__) | |___|  _ <\n /_/   \_\____|_____|  \____|\___/|_____|____/____/|_____|_| \_\ "
    print(epic_title)
    print("Made by Corbin Hibler")
    print("Guess the average age of a person's name!\n")
    manual_mode_input = input("Would you like to enter manual mode? (y/n): ")
    if manual_mode_input == 'y':
        manual_mode = True
        print("MANUAL MODE: ON\n")
    else:
        manual_mode = False
        print("Names will be given randomly from an API!")  

    if not manual_mode:
        country_mode_input = input("Would you like to enter a country code? Names will be generated from a specific country of your choosing. (y/n): ")
        if country_mode_input == 'y':
            country_mode = True
            country_code = input("Enter a country code (e.g. US, RU, MX, DE): ")
        else:
            country_mode = False

    points = 0     

    for i in range(0,10):
        if manual_mode: 
            name = input("\nEnter a name you would like to guess the age for: ")
        else:
            if country_mode: 
                name = get_name(country_code)
            else:
                name = get_name("US")
            
        guess = int(input(f"\nGuess the age of: {name}\nAge: "))
        age = get_age(name)
        if guess == age:
            print("EXACTLY CORRECT! +25 points!")
            points += 25
        else:
            difference = abs(guess - age);
            print("Off by: ", difference)
            print(name, " is actually ", age, " years old on average.")

            if difference == 1:
                print("+15 points!")
                points += 15
            elif difference == 2:                   
                print("+9 points!")
                points += 9
            elif difference == 3:
                print("+8 points!")
                points += 8
            elif difference == 4:
                print("+7 points!")
                points += 7
            elif difference == 5:
                print("+6 points!")
                points += 6

    print("YOU EARNED", points, "POINTS!")

# Access's Name Parser's awesome random name API
def get_name():
    api_key = "-------insert api key-------"
    url = f"https://api.parser.name/?api_key={api_key}&endpoint=generate"
    response = requests.get(url)

    if response.status_code == 200:
        json = response.json()
        name = json['data'][0]['name']['firstname']['name_ascii']
        return name
    else:
        print("API Error:" + response.status_code)
        return None

# Access Name Parser's random name API, this time from a specific country
def get_name(country_code):
    api_key = "-------insert api key---------"
    url = f"https://api.parser.name/?api_key={api_key}&endpoint=generate&country_code={country_code}"
    response = requests.get(url)

    if response.status_code == 200:
        json = response.json()
        name = json['data'][0]['name']['firstname']['name_ascii']
        return name
    else:
        print("API Error:" + response.status_code)
        return None

# Accesses an API that returns the average age of a name
def get_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        age = response.json().get('age')
        return age
    else:
        print("API Error:" + response.status_code)
        return None

if __name__ == "__main__":
    main()
