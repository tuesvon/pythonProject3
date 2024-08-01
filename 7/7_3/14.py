# Only even numbers
even = True
for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        even = False

if even:
    print('YES')
else:
    print('NO')