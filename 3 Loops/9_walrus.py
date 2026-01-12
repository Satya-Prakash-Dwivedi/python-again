value = 13

if remainder := value % 5:
    print(f"Not completely divisible , remainder is {remainder}")

flavours = ["Masala", "Ginger", "Lemon", "Tulsi"]

print(f"Available flavours : {flavours}")

while(flavour := input("Choose your chai flavour : ")) not in flavours:
    print(f"Sorry , {flavour} is not available")

print(f"You choose {flavour} flavour")