print("ATM Cash Dispenser")
total100 = total50 = total20 = total10 = total1 = 0
customersserved = 0
totaldispensed = 0
serving = True

while serving:
    name = input("Enter your name")
    amount = int(input(f"Hello {name}, how much money would you like to withdraw"))
    if amount <=0:
        print("Invalid amount")
        continue
    print(f"Dispensing amount {amount} units for {name}")
    remaining = amount
    index = 1

    while index<= 5:
        if index == 1:
            value = 100
        elif index == 2:
            value = 50
        elif index == 3:
            value = 20
        elif index == 4:
            value = 10
        else:
            value = 1
        count = remaining // value
        if count>0:
            print(f"{count} * {value} = {count * value}")
            remaining -= count*value
            if value == 100:
                total100 += count
            elif value == 50:
                total50 += count
            elif value == 20:
                total20 += count
            elif value == 10:
                total10 += count
            else:
                total1 += count
        index += 1
    customersserved += 1
    totaldispensed += amount
    print("Transaction Complete")
    again = input("Do you want to try again")
    if again == "no":
        serving = False