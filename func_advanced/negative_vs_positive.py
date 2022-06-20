nums = [int(x) for x in input().split()]

negative = []
positive = []

for num in nums:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

sum_negatives = sum(negative)
print(sum_negatives)
sum_positives = sum(positive)
print(sum_positives)

if abs(sum_negatives) > abs(sum_positives):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')
