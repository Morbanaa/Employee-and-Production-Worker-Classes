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
                print("(C) Exit Program:")
                choice = input("Choose: ").upper()

                match choice:
                    case "A":
                        pass
                    case "B":
                        pass
                    case "C":
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
                        collect_data(workers)
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
        counter += 1
        while True:
            name = input(f"Enter employee name #{counter}: ").upper()
            if name != "" and name != " ":
                clear_screen()
                break

        while True:
            try:
                number = int(input(f"Enter employee number #{counter}: "))
                clear_screen()
                break
            except ValueError:
                print("Must be a valid none decimal number!")

        while True:
            try:
                shift_number = int(input(f"Enter employee shift number #{counter}: "))
                clear_screen()
                break
            except ValueError:
                print("Must be a valid none decimal number!")

        while True:
            try:
                pay_rate = float(input(f"Enter employee pay_rate #{counter}: "))
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
            break
    display(workers)



# Accepts list of worker objects and iterates over them printing them calling the display method
def display(workers):
    print("Name ---------- Number ---------- Shift Number ---------- Pay Rate")
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