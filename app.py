from wine import Wine
import os.path
import pandas as pd
from tabulate import tabulate


def print_menu():
    # Print options to the user
    print("Please choose from one of the following options...")
    print("1. Enter features")
    print("2. import from csv")
    print("0. Exit")


def input_features(wine):
    try:
        fixed_acidity = float(input("Enter fixed acidity: "))
        wine.set_fixed_acidity(fixed_acidity)

        volatile_acidity = float(input("Enter volatile acidity: "))
        wine.set_volatile_acidity(volatile_acidity)

        citric_acid = float(input("Enter citric acid: "))
        wine.set_citric_acid(citric_acid)

        residual_sugar = float(input("Enter residual sugar: "))
        wine.set_residual_sugar(residual_sugar)

        chlorides = float(input("Enter chlorides: "))
        wine.set_chlorides(chlorides)

        free_sulfur_dioxide = float(input("Enter free sulfur dioxide: "))
        wine.set_free_sulfur_dioxide(free_sulfur_dioxide)

        total_sulfur_dioxide = float(input("Enter total sulfur dioxide: "))
        wine.set_total_sulfur_dioxide(total_sulfur_dioxide)

        density = float(input("Enter density: "))
        wine.set_density(density)

        pH = float(input("Enter pH: "))
        wine.set_pH(pH)

        sulphates = float(input("Enter sulphates: "))
        wine.set_sulphates(sulphates)

        alcohol = float(input("Enter alcohol: "))
        wine.set_alcohol(alcohol)

        wine.print_wine_attributes()
    except Exception as e:
        # print("Invalid input")
        print("An exception occurred: ", e)


def input_csv_path():
    while True:
        csv_path = input(
            "Please enter the path to the CSV file containing wine data, or type 'exit' to go back to main menu: ")
        if csv_path.lower() == "exit":
            break
        if not os.path.exists(csv_path):
            print("File not found, please enter a valid file path.")
        else:
            try:
                df = pd.read_csv(csv_path, sep=";")
                print(
                    "Data successfully loaded from CSV file.\n Here are the first five rows from the CSV file.\n")
                # display first 5 rows of the DataFrame
                print(tabulate(df.head(),  headers='keys', showindex=False,
                      tablefmt='fancy_grid',  numalign="center", stralign="center"))
                break
            except Exception as e:
                print("An exception occurred: ", e)


if __name__ == "__main__":
    wine = Wine()
    option = -1

    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again.")

        if (option == 1):
            input_features(wine)
        elif (option == 2):
            input_csv_path()
        elif (option == 0):
            break
        else:
            option = 0

print("\n\033[32mThank you for using wine prediction system. We hope you'll come back soon! \033[0m\n")
