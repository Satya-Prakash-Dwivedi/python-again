staff = [("Satya", 17), ("Steve", 16), ("David", 15)]

for name , age in staff:
    if (age >= 18):
        print(f"{name} is eligible for managing staff")
        break
else:
    print("None of the staff is eligible for manager position")