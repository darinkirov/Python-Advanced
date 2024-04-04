def even_odd(*args, command):
    if command == "even":
        return [num for num in args if num % 2 == 0]
    elif command == "odd":
        return [num for num in args if num % 2 != 0]
    else:
        return "Invalid command"
