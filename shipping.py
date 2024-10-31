weight = float(input("Enter the weight of your package: "))
if weight == "" or weight <= 0:
  print("Please check your weight and try again")
else:
  print("Indianapolis Shipping Depot:")
  print("The cost, based on the weight you provided of " + str(weight) + " lbs. is:" + "\n")
#ground shipping
  if weight <= 2:
    ground_cost = (weight * 1.50) + 20.00
    print("Ground Shipping Costs $" + str(ground_cost))
  elif weight > 2 and weight <= 6:
    ground_cost = (weight * 3.00) + 20.00
    print("Ground Shipping Costs $" + str(ground_cost))
  elif weight > 6 and weight <= 10:
    ground_cost = (weight * 4.00) + 20.00
    print("Ground Shipping Costs $" + str(ground_cost))
  elif weight > 10:
    ground_cost = (weight * 4.75) + 20.00
    print("Ground Shipping Costs $" + str(ground_cost))

#premium ground shipping
  premium = 125.00

  print("Premium Ground Shipping Costs $" + str(premium))

#drone shipping
  if weight <= 2:
    drone_cost = (weight * 4.50)
    print("Drone Shipping Costs $" + str(drone_cost) + "\n")
  elif weight > 2 and weight <= 6:
    drone_cost = (weight * 9.00)
    print("Drone Shipping Costs $" + str(drone_cost) + "\n")
  elif weight > 6 and weight <= 10:
    drone_cost = (weight * 12.00)
    print("Drone Shipping Costs $" + str(drone_cost) + "\n")
  elif weight > 10:
    drone_cost = (weight * 14.25)
    print("Drone Shipping Costs $" + str(drone_cost) + "\n")

  print("To Save You The Most Money:")

  if ground_cost < premium and drone_cost:
    print("Go with Ground Shipping!")
  elif premium < ground_cost and drone_cost:
    print("Go with Premium Ground Shipping!")
  else:
    print("Go with Drone Shipping!")
