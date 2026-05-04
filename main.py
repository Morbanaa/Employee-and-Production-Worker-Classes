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
            number = input(f"Enter number #{counter}: ").upper()
            if number != "" and number != " ":
                break

        while True:
            shift_number = input(f"Enter shift number #{counter}: ").upper()
            if shift_number != "" and shift_number != " ":
                break

        while True:
            pay_rate = input(f"Enter payrate #{counter}: ").upper()
            if pay_rate != "" and pay_rate != " ":
                break

        choice = input("Would you like to enter another input?(Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            continue
        else:
            break


if __name__ == "__main__":
    main()