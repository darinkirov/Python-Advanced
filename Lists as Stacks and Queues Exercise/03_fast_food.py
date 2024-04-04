from collections import deque


def serve_customers(food_quantity, orders):
    orders_queue = deque(orders)
    max_order = max(orders)

    while orders_queue:
        current_order = orders_queue[0]
        if food_quantity >= current_order:
            food_quantity -= current_order
            orders_queue.popleft()
        else:
            break

    if not orders_queue:
        print(max_order)
        print("Orders complete")
    else:
        print(max_order)
        print("Orders left:", ' '.join(map(str, orders_queue)))


if __name__ == "__main__":
    food_quantity = int(input())
    orders = list(map(int, input().split()))
    serve_customers(food_quantity, orders)
