from classes import Production_Worker

def main():
    workers = []

    counter = 0
    while True:
        counter += 1
        while True:
            name = input(f"Enter name #{counter}: ").upper()
            if name != "" and name != " ":
                break

        while True:
            try:
                number = int(input(f"Enter number #{counter}: "))
                break
            except ValueError:
                print("Must be a valid number!")

        while True:
            shift_number = input(f"Enter shift number #{counter}: ")
            try:
                shift_number = int(shift_number)
            except ValueError:
                print("Must be a valid number!")
            if shift_number:
                break

        while True:
            pay_rate = input(f"Enter payrate #{counter}: ")
            try:
                pay_rate = float(pay_rate)
            except ValueError:
                print("Must be a valid number!")
            if pay_rate:
                break

        choice = input("Would you like to enter another input?(Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            continue
        else:
            break


if __name__ == "__main__":
    main()