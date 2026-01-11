chai_order = dict(type="Masala chai", size="large", sugar=2)
print(f"Chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Chai recipe : {chai_recipe}")

print(f"Is sugar in chai order {'sugar' in chai_order}")

chai_order = {"type" : "Ginger chai", "size" : "Medium" , "sugar" : 1}
print(f"Order details (keys) : {chai_order.keys()}")
print(f"Order details (values) : {chai_order.values()}")
print(f"Order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last removed : {last_item}")

extra_spices = {"cardamom" : "crushed", "ginger" : "sliced"}
chai_order.update(extra_spices)
print(f"Chai order updated : {chai_order}")

customer_note = chai_order.get('size' , "No note")
print(f"Customer note is : {customer_note}")
