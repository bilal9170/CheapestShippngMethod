def ground_shipping_cost(weight):

  if weight <= 2:
    price = 1.50
  elif weight <= 6:
    price = 3.00
  elif weight <= 10:
    price = 4.00
  else:
    price = 4.75
   
  return 20 + (price * weight)

print(ground_shipping_cost(8.4))


premium_shipping = 125

def drone_shipping_cost(weight):
  if weight <= 2:
    price = 4.50
  elif weight <=6:
    price = 9.00
  elif weight <= 10:
    price = 12.00
  elif weight > 10:
    price = 14.25

  return price * weight + 0.00

print(drone_shipping_cost(4))

def cheapest_cost(weight):

  ground = ground_shipping_cost(weight)
  drone = drone_shipping_cost(weight)
  premium = premium_shipping

  if ground < drone and ground < premium:
    method = "Ground"
    cost = ground
  elif drone < ground and drone < premium:
    method = "Drone"
    cost = drone
  else:
    method = "Premium"
    cost = premium 


  print("The cheapest method is %s and the cost is $%.2f."
        % (method, cost) 
        )

cheapest_cost(41.5)
