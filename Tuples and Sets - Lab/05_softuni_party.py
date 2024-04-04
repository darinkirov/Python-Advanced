def process_guests(N, reservation_codes):
    vip_guests = set()
    regular_guests = set()

    for i in range(N):
        code = reservation_codes[i]
        if code[0].isdigit():
            vip_guests.add(code)
        else:
            regular_guests.add(code)

    arrived_guests = {"VIP": set(), "Regular": set()}
    while True:
        guest = input().strip()
        if guest == "END":
            break
        if guest in vip_guests:
            arrived_guests["VIP"].add(guest)
        elif guest in regular_guests:
            arrived_guests["Regular"].add(guest)

    return arrived_guests


if __name__ == "__main__":
    N = int(input("Enter the number of guests: "))
    reservation_codes = [input().strip() for _ in range(N)]

    guests = process_guests(N, reservation_codes)

    not_arrived_vip = sorted(guests["VIP"] - guests["VIP"])
    not_arrived_regular = sorted(guests["Regular"] - guests["Regular"])

    if not_arrived_vip:
        print(len(not_arrived_vip))
        for guest in not_arrived_vip:
            print(guest)

    if not_arrived_regular:
        print(len(not_arrived_regular))
        for guest in not_arrived_regular:
            print(guest)
