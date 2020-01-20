temps = [221, 234, 340, 230]

new_temps = [temp / 10 for temp in temps]

print(new_temps)

temps2 = [221, 234, 340, -9999, 230]

new_temps2 = [temp / 10 for temp in temps2 if temp != -9999]

print(new_temps2)

temps3 = [221, 234, 340, -9999, 230]

new_temps3 = [temp / 10 if temp != -9999 else 0 for temp in temps3]

print(new_temps3)