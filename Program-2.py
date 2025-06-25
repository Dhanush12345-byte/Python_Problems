def generate_odd_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

# Example
a = 4
print("Output:", generate_odd_series(a))  # Output: [1, 3, 5, 7]
