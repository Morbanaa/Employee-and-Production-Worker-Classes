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
            try:
                shift_number = int(input(f"Enter shift number #{counter}: "))
                break
            except ValueError:
                print("Must be a valid number!")

        while True:
           try:
                pay_rate = int(input(f"Enter pay_rate #{counter}: "))
                break
           except ValueError:
                print("Must be a valid number!")
        
        # Creates worker object and adds to list workers
        workers.append(Production_Worker(name,number,shift_number,pay_rate))

        # Asks user if they want to input more data
        choice = input("Would you like to enter another input?(Y/N) ").upper()
        if choice == "Y" or choice == "YES":
            continue
        else:
            break
    display(workers)

def display(workers):
    print("Name ---------- Number ---------- Shift Number ---------- Pay Rate")
    for worker in workers:
        worker.display()


if __name__ == "__main__":
    main()