from collections import deque

def process_customers():
    queue = deque()
    while True:
        command = input().strip()
        if command == "End":
            print(f"{len(queue)} people remaining.")
            break
        elif command == "Paid":
            while queue:
                print(queue.popleft())
        else:
            queue.append(command)

if __name__ == "__main__":
    process_customers()
