numbers = list(map(int, input().split()))

positives = [num for num in numbers if num > 0]
negatives = [num for num in numbers if num < 0]

sum_negatives = sum(negatives)
sum_positives = sum(positives)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
elif sum_positives > abs(sum_negatives):
    print("The positives are stronger than the negatives")
