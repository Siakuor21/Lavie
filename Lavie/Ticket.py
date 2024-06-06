import json

# Database to store user credentials
user_credentials = {
    "admin": "password"
}

# Database to store locations
locations = []

# Database to store reservations
reservations = []

# Function to verify user credentials
def verify_login(username, password):
    return user_credentials.get(username) == password

# Function to display main menu
def display_main_menu():
    print("\n----------- MENU -----------")
    print("1. Location")
    print("2. Reservation")
    print("3. Save data")
    print("4. Exit")

# Function to display location sub-menu
def display_location_menu():
    print("\n----------- LOCATION -----------")
    print("1. Add new location")
    print("2. Remove a location")
    print("3. Back")
    print("4. Exit")

# Function to add a new location to the database
def add_location():
    print("\n ADD NEW LOCATION ")
    name = input("Enter location name: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    single_price = float(input("Enter price for a single room: "))
    double_price = float(input("Enter price for a double room: "))
    discount = float(input("Enter discount percentage: "))
    
    location = {
        "Name": name,
        "City": city,
        "Country": country,
        "Single Price": single_price,
        "Double Price": double_price,
        "Discount": discount
    }
    
    locations.append(location)
    print("Location added successfully.")

# Function to remove a location from the database
def remove_location():
    print("\n----------- REMOVE LOCATION -----------")
    name = input("Enter location name to remove: ")
    for location in locations:
        if location["Name"] == name:
            locations.remove(location)
            print("Location removed successfully.")
            return
    print("Location not found.")

# Function to save data to file
def save_data():
    with open("data.json", "w") as file:
        json.dump({"locations": locations, "reservations": reservations}, file)
    print("Data saved successfully.")

# Function to handle reservation
def make_reservation():
    print("\n----------- RESERVATION -----------")
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    date = input("Enter reservation date (YYYY-MM-DD): ")
    time = input("Enter reservation time (HH:MM): ")
    location = input("Enter location name: ")
    room_type = input("Enter room type (single/double): ")
    num_rooms = int(input("Enter number of rooms: "))
    
    for loc in locations:
        if loc["Name"] == location:
            if room_type == "single":
                price = loc["Single Price"] * num_rooms
            elif room_type == "double":
                price = loc["Double Price"] * num_rooms
            else:
                print("Invalid room type.")
                return
            price -= price * (loc["Discount"] / 100)  # Apply discount
            reservation = {
                "Name": name,
                "Phone Number": phone_number,
                "Date": date,
                "Time": time,
                "Location": location,
                "Room Type": room_type,
                "Number of Rooms": num_rooms,
                "Total Price": price
            }
            reservations.append(reservation)
            print("Reservation made successfully.")
            return
    print("Location not found.")

# Main function
def main():
    print("Welcome to Lavie Traveling and Tour Ticket Reservation System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if verify_login(username, password):
        print("Login successful. Welcome, {}!".format(username))
        while True:
            display_main_menu()
            choice = input("Choose option (1-4): ")
            if choice == '1':
                while True:
                    display_location_menu()
                    loc_choice = input("Choose option (1-4): ")
                    if loc_choice == '1':
                        add_location()
                    elif loc_choice == '2':
                        remove_location()
                    elif loc_choice == '3':
                        break
                    elif loc_choice == '4':
                        print("Exiting...")
                        exit()
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
            elif choice == '2':
                make_reservation()
            elif choice == '3':
                save_data()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
