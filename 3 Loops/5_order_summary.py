names = ["Satya", "Hitesh", "David", "Vivekananda", "Steve", "Osho"]
bills = [300, 400, 250, 120, 850, 1000]

for name, bill in zip(names, bills):
    print(f"{name} paid {bill} rupees")