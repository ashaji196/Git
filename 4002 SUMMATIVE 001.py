import csv

number_plate = []

def add_to_file():
    input_car_reg = input("Add a car reg: ")
    number_plate.append(input_car_reg)
    print(f"the number '{input_car_reg}'1 has successfully been added.")


def display_carreg_from_file():
    if len(number_plate) == 0:
        print("List is empty")
    else:
        for i in range(len(number_plate)):
            print(f"Index {i}: {number_plate[i]}")

def display_specific_item():
    user_input = input("please enter your index number to find your car: ")
    if user_input.isdigit():
        index = int(user_input)
        if 0 <= index < len(number_plate):
            print(f"Index {index}: {number_plate[index]}")
        else:
            print("Error: Index not within range.")
    else:
        print("Error: Please enter a valid whole number.")

def bulk_upload():
    filename = input("Please input file name of csv: ")
    try:
            with open(filename, 'r') as file:
                for line in file:
                    items = line.strip().split(',')
                    for item in items:
                        if item:
                            number_plate.append(item.strip())
            print("UUpload has been successfully completed complete.")
    except Exception as e:
            print(f"An error occurred while reading the file: {e}")

def present_info():
    output_filename = "Car-reg-List.txt"
    try:
        with open(output_filename, 'w') as file:
            file.write("Car Dealership Inventory List\n")
            file.write("")
            for car in number_plate:
                file.write(f"{car}\n")
        print(f"data has been to '{output_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    while True:
        print("---------------------------------")        
        print("CAR DEALERSHIP MANAGEMENT SYSTEM")
        print("---------------------------------")
        print("1. Add a car to the list")
        print("2. Print all cars to the screen")
        print("3. Print a single car using index")
        print("4. Add a batch of cars (Bulk Upload)")
        print("5. Download list to file")
        print("6. Quit")
        print("")
        
        choice = input("Please enter your choice (1-6): ")
        
        if choice == '1':
            add_to_file()
        elif choice == '2':
            display_carreg_from_file()
        elif choice == '3':
            display_specific_item()
        elif choice == '4':
            bulk_upload()
        elif choice == '5':
            present_info()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()
