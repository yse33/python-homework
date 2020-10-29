i = 2000
while i < 5000:
    a = i // 10
    b = i // 100
    c = i // 1000
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and i % 2 == 0:
        print(i, end = ", ")

    i += 1




