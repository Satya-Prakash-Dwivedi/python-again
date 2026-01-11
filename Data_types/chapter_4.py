# Tuples and membership testing

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # upcasting
print(f"Total actions : {total_actions}")

milk_present = 0
print(f"Is there milk {bool(milk_present)}")

water_add = True
milk_add = True

can_server_chai = water_add and milk_add
print(f"Can server chai : {can_server_chai}")