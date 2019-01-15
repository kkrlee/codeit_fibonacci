COUNT = 20

current = 1
previous = 0
i = 0

while i < COUNT:
    print(current)

    temp = previous
    previous = current
    current += temp

    i += 1
