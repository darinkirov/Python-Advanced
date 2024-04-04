def unique_usernames(N):
    unique_usernames_set = set()

    for _ in range(N):
        username = input().strip()
        unique_usernames_set.add(username)

    return unique_usernames_set


if __name__ == "__main__":
    N = int(input("Enter the number of usernames: "))
    unique_usernames_set = unique_usernames(N)

    for username in unique_usernames_set:
        print(username)
