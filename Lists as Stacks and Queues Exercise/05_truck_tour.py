def find_starting_point(petrol_pumps):
    total_petrol = 0
    starting_point = 0
    petrol_needed = 0

    for i in range(len(petrol_pumps)):
        petrol, distance = petrol_pumps[i]

        total_petrol += petrol - distance

        if total_petrol < 0:
            petrol_needed -= total_petrol
            total_petrol = 0
            starting_point = i + 1

    return starting_point


if __name__ == "__main__":
    N = int(input())
    petrol_pumps = []
    for _ in range(N):
        petrol, distance = map(int, input().split())
        petrol_pumps.append((petrol, distance))

    starting_point = find_starting_point(petrol_pumps)
    print(starting_point)
