def parking_lot_status(commands):
    parking_lot = set()
    for command in commands:
        direction, car_number = command.split(", ")
        if direction == "IN":
            parking_lot.add(car_number)
        elif direction == "OUT":
            if car_number in parking_lot:
                parking_lot.remove(car_number)

    if parking_lot:
        for car_number in parking_lot:
            print(car_number)
    else:
        print("Parking Lot is Empty")

if __name__ == "__main__":
    N = int(input("Enter the number of commands: "))
    commands = [input() for _ in range(N)]
    parking_lot_status(commands)
