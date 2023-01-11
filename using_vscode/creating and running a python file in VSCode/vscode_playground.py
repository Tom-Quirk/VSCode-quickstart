#necessary user information
weight = float(input("Insert the weight of your package in lbs: "))

#ground shipping pricing
if weight <= 2.0:
  ground_shipping_price = (weight*1.5) + 20
elif weight <= 6.0:
  ground_shipping_price = (weight*3.0) + 20
elif weight <= 10.0:
  ground_shipping_price = (weight*4.0) + 20
else:
  ground_shipping_price = (weight*4.75) + 20
  
#ground shipping premium price
ground_shipping_premium_price = 125.00

#drone shipping price
if weight <= 2.0:
  drone_shipping_price = weight*4.5
elif weight <= 6.0:
  drone_shipping_price = weight*9.0
elif weight <= 10.0:
  drone_shipping_price = weight*12.0
else:
  drone_shipping_price = weight*14.25

#code to decide which is the cheapest choice
if ground_shipping_price <= drone_shipping_price and ground_shipping_price <= ground_shipping_premium_price:
  print("Ground shipping is the cheapest option")
  print(ground_shipping_price)

if drone_shipping_price <= ground_shipping_price and drone_shipping_price <= ground_shipping_premium_price:
  print("Drone shipping is the cheapest option")
  print(drone_shipping_price)

if ground_shipping_premium_price <= ground_shipping_price and ground_shipping_premium_price <= drone_shipping_price: 
  print("Ground shipping premium is the cheapest option")
  print(ground_shipping_premium_price)

