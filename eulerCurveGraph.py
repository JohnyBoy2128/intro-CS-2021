import simpleplot

cords = []
y = 0

for i in range(1, 100):
    x = (1 + (1 / i) ** i)
    y += 0.1
    cords.append((x, y))

print(cords)