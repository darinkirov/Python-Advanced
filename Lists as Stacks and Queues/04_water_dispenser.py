from collections import deque


def track_water():
    water_quantity = int(input())
    queue = deque()

    while True:
        command = input().strip()
        if command == "Start":
            break
        else:
            queue.append(command)

    while True:
        command = input().split()
        if command[0] == "End":
            break
        elif command[0] == "refill":
            liters = int(command[1])
            water_quantity += liters
        else:
            person_name = queue.popleft()
            liters = int(command[0])
            if water_quantity >= liters:
                print(f"{person_name} got water")
                water_quantity -= liters
            else:
                print(f"{person_name} must wait")

    print(f"{water_quantity} liters left")


if __name__ == "__main__":
    track_water()
