print("get started")
try:
    x = int(input("Number: "))
except ValueError:
    x = 0
for i in range(x):
    print(f"Lol-{i}")

