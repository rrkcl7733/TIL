x, y, n = map(int, input().split())
for i in range(1, n + 1):
    print('FizzBuzz' if not i % x and not i % y else 'Fizz' if not i % x else 'Buzz' if not i % y else i)
