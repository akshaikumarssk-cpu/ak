def generate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence[:n]

# Print the first 10 Fibonacci numbers
print(generate_fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
