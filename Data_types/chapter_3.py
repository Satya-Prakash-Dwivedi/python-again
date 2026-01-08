# string = Index, slice and encoding

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams : {total_grams}")

remaining_grams = black_tea_grams - ginger_grams
print(f"Remaining grams : {remaining_grams}")

milk_litres = 7
servings = 3

milk_per_serving = milk_litres / servings
print(f"Milk per servings : {milk_per_serving}")

tea_bags = 7
pots = 3
tea_bags_per_pot = tea_bags // pots
print(f"Tea bags per pot : {tea_bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Left over pods are {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"The powerful flavor is : {powerful_flavor}")

total_tea_leaves = 1_000_000_000
print(f"Total tea leaves harvested : {total_tea_leaves}")