numbers = list(map(int, input().split(", ")))
result = 1

for i in range(len(numbers)):
    if numbers[i] <= 5:
        result *= numbers[i]
    elif numbers[i] > 5 and numbers[i] <= 10:
        if numbers[i] != 0:
            result /= numbers[i]

print(result)
