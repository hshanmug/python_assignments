Backyard_length = float(input("Length of Backyard: "))
Backyard_Width = float(input("Width of Backyard: "))
Backyard_area = Backyard_length * Backyard_Width
print('Area is:',round(Backyard_area,2))

total_flowers = int(input("How many flowers? "))
rows_colums = int(total_flowers**(1/2))
print('Each Row and Column of the Centerpiece should have',rows_colums,'Flowers')

triangle_base = float(input('Base of Tent: '))
triangle_height = float(input('Height of Tent: '))
triangle_area = (1/2) * triangle_base * triangle_height
print('The tent area is:',round(triangle_area,2))

banner_length = float(input('Length of Banner: '))
yard_perimeter = float(input('Length of Yard Perimeter: '))
number_banners = int(yard_perimeter / banner_length)
print('You need',number_banners,'banners')

sandwich_price = float(input("Price of Sandwich $: "))
pizza_price = float(input('Price of Pizza $: '))
total_guests = int(input('Total Guests: '))
total_sandwich = (sandwich_price * total_guests) 
sandwich_final = total_sandwich + (total_sandwich * 0.02) + 5.00
total_pizza = (pizza_price * total_guests) / 6
pizza_final = total_pizza + (total_pizza * 0.02) + 5.00
print('Total Sandwich Price $:',round(sandwich_final,2))
print('Total Pizza Price $:',round(pizza_final,2))
print('The cheaper price is $:',min(round(sandwich_final,2),round(pizza_final,2)))