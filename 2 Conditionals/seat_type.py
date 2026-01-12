seat = input("Enter your preferred seat type : 'General / AC / Sleeper / Luxury : ").lower()

match seat:
    case 'sleeper':
        print(f"Sleeper - No AC, beds available")
    case 'ac' :
        print(f"AC - Air conditioned, comfy ride")
    case 'general':
        print("General - Cheapest option, no reservation")
    case 'luxury':
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")