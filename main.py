# Teddy Rodd
# Morbanaa Studios
# Lab 11
# Employee and Production Worker Classes

import dis
from classes import Production_Worker
import platform
import os

def main():
    workers = []
    has_data = False
    while True:

        # Decide if outside loop continues
        while True:
            #Only runs this if there is no data
            if has_data == True:
                print("Would you like to:")
                print("(A) Change any values:")
                print("(B) Clear Data:")
                print("(C) Print Data:")
                print("(D) Exit Program:")
                choice = input("Choose: ").upper()

                match choice:
                    case "A":
                        clear_screen()
                        workers = change_values(workers)
                    case "B":
                        clear_screen()
                        workers = clear_data(workers)
                        has_data = False
                    case "C":
                        clear_screen()
                        display(workers)
                    case "D":
                        clear_screen()
                        break
                    case _:
                        clear_screen()
                        print("Not a valid input!")
                        continue

            # runs if data is already there
            else:
                print("Would you like to:")
                print("(A) Add data:")
                print("(B) Exit Program:")
                choice = input("Choose: ").upper()

                match choice:
                    case "A":
                        has_data = True
                        clear_screen()
                        workers = collect_data(workers)
                    case "B":
                        clear_screen()
                        break
                    case _:
                        clear_screen()
                        print("Not a valid input!")
                        continue
        break
       

def collect_data(workers):
    counter = 0
    while True:
        while True:
            name = input(f"Enter employee name: ").upper()
            if name != "" and name != " ":
                clear_screen()
                break

        while True:
            try:
                number = int(input(f"Enter employee number: "))
                clear_screen()
                break
            except ValueError:
                print("Must be a valid none decimal number!")

        while True:
            try:
                shift_number = int(input(f"Enter employee shift number (1 = Day Shift || 2 = Night Shift): "))
                if shift_number == 1 or shift_number == 2:
                    clear_screen()
                    break
                else:
                    print("You may only enter 1 or 2!")
                    continue
            except ValueError:
                print("Must be a valid none decimal number!")

        while True:
            try:
                pay_rate = float(input(f"Enter employee pay_rate: "))
                clear_screen()
                break
            except ValueError:
                print("Must be a valid decimal number!")
        
        # Creates worker object and adds to list workers
        workers.append(Production_Worker(name,number,shift_number,pay_rate))

        # Asks user if they want to input more data
        choice = input("Would you like to enter another input?(Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            clear_screen()
            continue
        else:
            clear_screen()
            return workers



# Change values in list of objects
def change_values(workers):
    while True:
        # Prints out table
        display(workers)

        # Deterims if person is in list
        target_name = input("Enter the name of whom you want to edit or Q to quit: ").upper()
        did_find = False
        for worker in workers:
            if worker.get_name() == target_name:
                did_find = True
                break
        if target_name == "Q" or target_name == "QUIT":
            clear_screen()
            break
        elif did_find == False:
            print("\nName not found!\n")
            continue
        else:
            # Determins which value the user would like to update in the object
            while True:
                print("\nWould you like to:")
                print("(A) Change the employee name:")
                print("(B) Change the employee number: ")
                print("(C) Change the employee shift number:")
                print("(D) Change the employee pay rate:")
                print("(E) Return to menu: ")
                choice = input("Choose: ").upper()

                match choice:
                    case "A":
                        while True:
                            name = input(f"\nEnter new employee name: ").upper()
                            if name != "" and name != " ":
                                clear_screen()
                                for worker in workers:
                                    if worker.get_name() == target_name:
                                        worker.set_name(name)
                                        break
                                break
                    case "B":
                        while True:
                            try:
                                number = int(input(f"\nEnter new employee number: "))
                                clear_screen()
                                for worker in workers:
                                    if worker.get_name() == target_name:
                                        worker.set_number(number)
                                        break
                                break
                            except ValueError:
                                print("Must be a valid none decimal number!")
                    case "C":
                        while True:
                            try:
                                shift_number = int(input(f"\nEnter new employee shift number (1 = Day Shift || 2 = Night Shift): "))
                                clear_screen()
                                for worker in workers:
                                    if worker.get_name() == target_name:
                                       worker.set_shift_number(shift_number)
                                       break
                                break
                            except ValueError:
                                print("Must be a valid none decimal number!")

                    case "D":
                        while True:
                            try:
                                pay_rate = float(input(f"\nEnter new employee pay_rate: "))
                                clear_screen()
                                for worker in workers:
                                    if worker.get_name() == target_name:
                                        worker.set_pay_rate(pay_rate)
                                        break
                                break
                            except ValueError:
                                print("Must be a valid decimal number!")
                    case "E":
                        clear_screen()
                        break
                    case _:
                        continue
                break
            break
    return workers


# Clears list of data
def clear_data(workers):
    workers.clear()
    return workers

# Accepts list of worker objects and iterates over them printing them calling the display method
def display(workers):
    print("Name ---------- Number ---------- Shift ---------- Pay Rate")
    for worker in workers:
        worker.display()
    print("__________________________________________________________________\n")


# Resets terminal for next step
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main()
    # Last message
    print("Have a great day!")