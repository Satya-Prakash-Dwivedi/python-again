masala_spice = ('cardamom', 'cloves', 'cinnamon')
(spice1, spice2, spice3) = masala_spice

print (f"Masala spice : {spice1, spice2, spice3}")

ginger_ratio , cardamom_ratio = 2 , 1
print(f"Ginger ratio : {ginger_ratio}, Cardamom ratio {cardamom_ratio}")
ginger_ratio , cardamom_ratio = cardamom_ratio , ginger_ratio
print(f"Ginger ratio : {ginger_ratio}, Cardamom ratio {cardamom_ratio}")

# Membership Testing

print(f"Is ginger in masala spice ? : {'cardamom' in masala_spice}")