from collections import deque


def hot_potato(kids, nth_toss):
    circle = deque(kids.split())

    while len(circle) > 1:
        for _ in range(nth_toss - 1):
            circle.rotate(-1)  # Pass the potato to the next kid
        removed_kid = circle.popleft()
        print(f"Removed {removed_kid}")

    print(f"Last is {circle[0]}")


if __name__ == "__main__":
    kids = input("Enter kids' names separated by space: ")
    nth_toss = int(input("Enter the nth toss: "))
    hot_potato(kids, nth_toss)
