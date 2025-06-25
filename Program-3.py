def conditional_odd_series(a):
    if a % 2 == 0:
        a -= 1
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result

# Example
a = 6
print("Output:", conditional_odd_series(a))  # Output: [1, 3, 5, 7, 9]
