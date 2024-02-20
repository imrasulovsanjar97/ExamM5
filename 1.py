def fibonacci_generator(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

fibonacci_gen = fibonacci_generator(int(input("n = ")))

print(list(fibonacci_gen))