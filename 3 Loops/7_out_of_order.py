flavours = ["Ginger", "Out of Stock", "lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if(flavour == "Out of Stock" ):
        continue
    if(flavour == "Discontinued"):
        break
    print(f"Chai flavour {flavour}")

print("Out of loop")