# Square root of a number

A = int(input())
root = -1
i = 1
while i * i <= A:
    if i * i == A:
        root = i
        break
    i += 1
print(root)