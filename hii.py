def max_fibonacciness(t, test_cases):
    results = []
    for a1, a2, a4, a5 in test_cases:
        # Compute the two candidate values for a3
        candidate1 = a4 - a2
        candidate2 = a5 - a4

        # Check Fibonacciness for candidate1
        count1 = 0
        if a4 == a1 + a2:
            count1 += 1
        if a5 == candidate1 + a4:
            count1 += 1
        if candidate1 == a4 - a2:
            count1 += 1

        # Check Fibonacciness for candidate2
        count2 = 0
        if a4 == a1 + a2:
            count2 += 1
        if a5 == candidate2 + a4:
            count2 += 1
        if candidate2 == a4 - a2:
            count2 += 1

        # Append the maximum Fibonacciness for this case
        results.append(max(count1, count2))

    return results

# Input handling
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Compute and output results
results = max_fibonacciness(t, test_cases)
for result in results:
    print(result)
