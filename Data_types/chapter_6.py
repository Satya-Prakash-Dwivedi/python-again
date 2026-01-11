chai_type = 'Ginger tea'
customer_name = 'Satya'

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = 'Aromatic and Bold'

print(f"First word : {chai_description[:8]}")
print(f"Last word : {chai_description[12:]}") # option + shift + down in order to copy the line below
print(f"Reverse word by word : {chai_description[::-1]}")

label_text = 'Spècial chai'
encoded_text = label_text.encode('utf-8')
decoded_text = encoded_text.decode('utf-8')
print(f'Non encoded label text : {label_text}')
print(f"Encoded text : {encoded_text}")
print(f"Decoded text : {decoded_text}")

