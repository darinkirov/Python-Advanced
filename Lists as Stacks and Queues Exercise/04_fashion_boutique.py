def calculate_racks(clothes, capacity):
    racks_used = 0
    current_rack_capacity = 0

    for cloth in clothes[::-1]:
        if current_rack_capacity + cloth <= capacity:
            current_rack_capacity += cloth
        else:
            racks_used += 1
            current_rack_capacity = cloth

    if current_rack_capacity > 0:
        racks_used += 1

    return racks_used


if __name__ == "__main__":
    clothes = list(map(int, input().split()))
    capacity = int(input())
    racks_needed = calculate_racks(clothes, capacity)
    print(racks_needed)
